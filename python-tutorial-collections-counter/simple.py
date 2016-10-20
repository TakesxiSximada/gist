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


counter = {}
for record in data:
    status = record.get('status', 'unknown')
    if status not in counter:
        counter[status] = 0
    counter[status] += 1

print(counter)
