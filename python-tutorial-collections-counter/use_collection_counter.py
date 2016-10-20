data = [
    {'tag': 'foo', 'second': 1, 'status': 'success'},
    {'tag': 'bar', 'second': 1, 'status': 'success'},
    {'tag': 'baz', 'second': 4, 'status': 'success'},
    {'tag': 'foo', 'second': 1, 'status': 'success'},
    {'tag': 'bar', 'second': 1, 'status': 'success'},
    {'tag': 'baz', 'second': 4, 'status': 'success'},
    {'tag': 'foo', 'second': 1, 'status': 'fail'},
    {'tag': 'bar', 'second': 1, 'status': 'success'},
    {'tag': 'baz', 'second': 4, 'status': 'success'},
    {'tag': 'foo', 'second': 1, 'status': 'fail'},
    {'tag': 'bar', 'second': 1, 'status': 'success'},
    {'tag': 'baz', 'second': 4, 'status': 'success'},
    {'tag': 'foo', 'second': 1, 'status': 'fail'},
    {'tag': 'bar', 'second': 1, 'status': 'success'},
    {'tag': 'baz', 'second': 4, 'status': 'success'},
]


import collections
counter = collections.Counter()
for record in data:
    counter.update([record.get('status', 'unknown')])
print(counter)
