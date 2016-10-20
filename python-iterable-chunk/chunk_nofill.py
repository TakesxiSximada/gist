
def groupper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip(*args)


def gen():
    for ii in range(10, 32):
        yield ii


for n in groupper(gen(), 5):
    print(list(n))
