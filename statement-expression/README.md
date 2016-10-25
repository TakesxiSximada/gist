# 式と文

プログラミング言語には式と文があります。

## Pythonの式と文

### 式

式はevalしたときになんらかの値を返す構文のことです。このなんらかの値はNone含みます。

#### 式の例

- `int(1)` は1を返すので式です。
- `1` は1を返すので式です。
- `"expression"` は"expression"を返すので式です。
- `(ii + 1 for ii in range(10))` はジェネレータオブジェクトを返すので式です。

#### 式じゃない例

- `a = 1`は何も返さないので式ではなりません。

  ```
  >>> eval('a = 1')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<string>", line 1
      a = 1
        ^
  SyntaxError: invalid syntax
  ```

- `for ii in range(10): pass` は何も返さないので式ではありません。


#### `print` は？

Python2とPython3ではprintの扱いが違います。
Python2ではprintは文です。そのためevalできません。

```
>>> eval('print 1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    print 1
        ^
SyntaxError: invalid syntax
>>> quit()
```

Python3ではprintは式になりました。そのためevalできます。

```
>>> eval('print(1)')
1
```
