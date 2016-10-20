# [Python] collections.Counterで数を数える

ログなどを集計していくと出現個数を数えたいときがあります。


```
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
```

例えばこのようなデータのstatusの数を数えるとします。

for文でその要素が出てきたらカウンタをインクリメントするコードは次のようになります。


```
>>> counter = {}
>>> for record in data:
...    status = record.get('status', 'unknown')
...    if status not in counter:
...        counter[status] = 0
...    counter[status] += 1
...
>>> print(counter)
{'success': 12, 'fail': 3}
```

## collections.Counter()を使う

collections.Counter()を使うと上記のコードを完結に書くことができます。

```
>>> import collections
>>>
>>> counter = collections.Counter()
>>> for record in data:
...    counter.update([record.get('status', 'unknown')])
...
>>> print(counter)
Counter({'success': 12, 'fail': 3})
```

初期化時に要素を渡すことが可能であれば、さらに完結に記述することができます。

```
>>> import collections
>>>
>>> counter = collections.Counter(record.get('status', 'unknown') for record in data)
>>> print(counter)
Counter({'success': 12, 'fail': 3})
```

collections.Counter()のドキュメントはこちら。
http://docs.python.jp/3/library/collections.html#collections.Counter
