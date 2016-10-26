# 並行(Concurrent)と並列(Pararel)

## 並行(Concurrent)

実行状態を複数保つことができる状態を並行と言います。正し同時に処理を実行することはできません。

```
* * * * * * * -+
               |
* * * * * * * -+
               | -> [Process]
* * * * * * * -+
               |
* * * * * * * -+
```

## 並列(Pararel)

複数の処理を同時に処理できることです。

```
* * * * * * * -+ -> [Process]

* * * * * * * -+ -> [Process]

* * * * * * * -+ -> [Process]

* * * * * * * -+ -> [Process]
```

## Pythonでよく使われる並行並列処理の分類

### 並行

- asyncio (coroutine含む)
- threading

### 並列

- multiprocessing
- subprocess
- celery
