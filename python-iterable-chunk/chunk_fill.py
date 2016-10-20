import itertools


def groupper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=None, *args)


def gen():
    for ii in range(10, 32):
        yield ii


for n in groupper(gen(), 5):
    print(list(n))
