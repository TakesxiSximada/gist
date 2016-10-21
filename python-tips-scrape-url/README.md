# review のコードの中からURLを抜き出す

ドキュメンテーションビルダーのreview形式で記述されたファイルからURLを抜き出します。

get_urls.py:

```
#! /usr/bin/env python
import sys
import re
import argparse


URL_PATTERN = '(?P<url>(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+))'

regx = re.compile(URL_PATTERN, re.I)


def get_urls(path):
    with open(path, 'rt', encoding='utf8') as fp:
        for line in fp:
            while line:
                matching = regx.search(line)
                if matching:
                    yield matching.group('url')
                    line = line[matching.end():]
                else:
                    line = ''


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('targets', nargs='+')
    args = parser.parse_args(argv)

    for target in args.targets:
        for url in get_urls(target):
            print(url)

if __name__ == '__main__':
    main()
```


次を解析用のファイルとします。

test.txt:

```
（@<i>{http://example.comy/one}）（@<i>{http://example.com/two/three}）（@<i>{https://example.com/Fish}）
（@<i>{https://python.org}）（@<i>{https://localhost:8000}）
```

引数にファイルパスを渡して実行します。

```
$ python get_urls.py test.txt
http://example.comy/one
http://example.com/two/three
https://example.com/Fish
https://python.org
https://localhost:8000
```
