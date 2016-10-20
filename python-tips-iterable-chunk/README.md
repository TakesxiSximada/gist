# iteratorをchunkに分ける

Pythonのドキュメントに記述があるのそのまま

## 不足している行はfillvalueでpaddingする

chunk_fill.py:

```
import itertools


def groupper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=None, *args)


def gen():
    for ii in range(30):
        yield ii


for n in groupper(gen(), 5):
    print(list(n))
```

## 不足している行は返さない返さない

chunk_nofill.py:

```
def groupper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip(*args)


def gen():
    for ii in range(10, 32):
        yield ii


for n in groupper(gen(), 5):
    print(list(n))

```


## 不足している行は不足している状態で返す

chunk_shortage.py:

```
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
```
