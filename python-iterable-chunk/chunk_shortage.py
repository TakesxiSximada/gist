import itertools


class StopChunkError(Exception):
    pass


def _go(iterable, fillvalue=StopChunkError):
    for elm in iterable:
        if elm is fillvalue:
            break
        yield elm


def chunk(iterable, n, fillvalue=StopChunkError):
    args = [iter(iterable)] * n
    zipped_iterable = itertools.zip_longest(fillvalue=fillvalue, *args)
    for elm in zipped_iterable:
        yield _go(elm, fillvalue)


for buf in chunk(range(32), 3):
    print(list(buf))
