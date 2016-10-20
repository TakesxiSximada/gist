#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import contextlib
import enum
import glob
import logging
import logging.config
import os
import re
import shutil
import sys
import tempfile

import six

import git
import gist

logger = logging.getLogger(__name__)


class SyncStatus(enum.Enum):
    created = 'created'
    updated = 'updated'
    fail = 'fail'
    ignore = 'ignore'


def setup_logging(conf_path=None):
    if conf_path is None:
        logging.basicConfig(
            format='[%(levelname)s] %(message)s',
            level=logging.INFO,
        )
        logging.debug('using default logger settings')
    else:
        logging.config.fileConfig(conf_path, disable_existing_loggers=False)
        logging.debug('using custom logger settings: %s', conf_path)


class TemporaryDirAdapter(object):
    def __init__(self, path):
        self.path = path

    def close(self):
        shutil.rmtree(self.path)


class ChangeDirectory(object):
    def __init__(self, path):
        self.original = os.getcwd()
        self.path = path
        os.chdir(path)

    def close(self):
        os.chdir(self.original)


def config_parser_factory(*args, **kwds):
    if six.PY3:
        klass = six.moves.configparser.ConfigParser
    else:
        klass = six.moves.configparser.SafeConfigParser

    return klass(*args, **kwds)


def get_gist_id(url):
    return url.split('/')[3]


def get_title_from_files(files):
    regx = re.compile('README.*$', re.I)
    for path in files:
        name = os.path.basename(path)
        if regx.match(name):
            with open(path, 'rb') as fp:
                return fp.readline() \
                         .decode() \
                         .lstrip('#') \
                         .strip()
    return 'no title'


def get_url(config, target):
    try:
        return config.get('gist-sync', 'url')
    except six.moves.configparser.NoSectionError:
        logger.debug('no section: create gist: %s', target)
        config.add_section('gist-sync')
    except six.moves.configparser.NoOptionError:
        logger.debug('no option: create gist: %s', target)


def get_files(config, target):
    try:
        files = list(map(
            lambda name: os.path.join(target, name.strip()),
            config.get('gist-sync', 'files').split()
        ))
    except six.moves.configparser.NoOptionError:
        files = []

    if not files:
        logger.warning('no files: add README.md: %s', target)
        for pattern in ('readme*', 'README*'):
            files.extend(
                glob.glob(
                    os.path.join(target, pattern)))
    return files


def get_title(config, target, files):
    try:
        title = config.get('gist-sync', 'title').strip()
    except six.moves.configparser.NoSectionError:
        logger.debug('no section: title: %s', target)
        config.add_section('gist-sync')
    except six.moves.configparser.NoOptionError:
        logger.debug('no option: title: %s', target)
    return title or get_title_from_files(files)


def sync_gist(target):
    if not os.path.isdir(target):
        logger.debug('ignore: not directory: %s', target)
        return SyncStatus.ignore.value, None

    gist_conf_path = os.path.join(target, 'gist.conf')
    if not os.path.isfile(gist_conf_path):
        logger.debug('ignore: not exist gist.conf: %s', target)
        return SyncStatus.ignore.value, None

    config = config_parser_factory()
    config.read(gist_conf_path)

    url = get_url(config, target)
    files = get_files(config, target)
    title = get_title(config, target, files)

    if url:  # update
        gist_id = get_gist_id(url)
        with contextlib.closing(TemporaryDirAdapter(tempfile.mkdtemp())) as tmpdir:
            cmd = ['clone', gist_id, tmpdir.path]
            gist.main(cmd)
            for filepath in files:
                shutil.copy(filepath, tmpdir.path)
            cur = os.getcwd()
            os.chdir(tmpdir.path)
            repo = git.Repo(search_parent_directories=True)
            filenames = [os.path.basename(filepath) for filepath in files]
            repo.index.add(filenames)
            repo.index.commit('update content')
            remote = repo.remote('origin')
            remote.push()
        os.chdir(cur)
        gist.main(['description', gist_id, title])
        return SyncStatus.updated.value, url
    else:  # create
        cmd = ['create', title, '--public']
        cmd.extend(files)
        url = gist.main(cmd)
        config.set('gist-sync', 'url', url)

        with open(gist_conf_path, 'w+t') as fp:
            config.write(fp)

        with contextlib.closing(ChangeDirectory(target)):
            conf_path = os.path.relpath(gist_conf_path, os.getcwd())
            repo = git.Repo(search_parent_directories=True)
            repo.index.add([conf_path])
            repo.index.commit('add gist.conf file')
            remote = repo.remote('origin')
            remote.push()
            return SyncStatus.created.value, url


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', default=None)
    parser.add_argument('targets', nargs='+')
    args = parser.parse_args(argv)
    setup_logging(args.conf)
    for target in args.targets:
        status, url = sync_gist(target)
        logger.info('sync finished: status=%s, url=%s', status, url)
    return 0

if __name__ == '__main__':
    rc = main()
    if rc is None or isinstance(rc, six.integer_types):
        sys.exit(rc)
    else:
        print(rc)
        sys.exit(0)
