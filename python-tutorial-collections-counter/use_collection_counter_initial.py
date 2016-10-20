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
counter = collections.Counter(record.get('status', 'unknown') for record in data)
print(counter)
