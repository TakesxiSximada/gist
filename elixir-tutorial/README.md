# Elixirチュートリアル

## インストール

OSXを前提にします。

```
＄brew install elixir
```

インストールが済んだらバージョンを確認してみます。

```
$ elixir -v
Erlang/OTP 19 [erts-8.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]

Elixir 1.3.4
```

## インタラクティブモード

iexコマンドでインタラクティブモードに入れます。


```
$ iex
Erlang/OTP 19 [erts-8.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]

Interactive Elixir (1.3.4) - press Ctrl+C to exit (type h() ENTER for help)
```

## Hello World

まずは `Hello World` と表示するプログラムを作成/実行します。

```
iex(3)> IO.puts "Hello world!!"
Hello world!!
:ok

```

Hello worldと表示されました。

インタラクティブモードから脱出します。脱出は`C-c`を入力した後に`a`です。

```
iex(11)>
BREAK: (a)bort (c)ontinue (p)roc info (i)nfo (l)oaded
       (v)ersion (k)ill (D)b-tables (d)istribution
a

```

次はファイルに記述して実行してみましょう。

hello_world.exs:

```
IO.puts "Hello World!!"
```

実行します。

```
$ elixir hello_world.exs
Hello World!!
```

表示されました。


## Concurrency

ElixirはErlangのVM上で動作するので並行処理が得意です。
Taskモジュールを使って子プロセスを実行してみましょう。

### 無名関数

`fn() -> ... end` で無名関数を定義できます。

```
iex(11)> foo = fn() -> "Hello" end
#Function<20.52032458/0 in :erl_eval.expr/5>
```

関数を実行します。

```
iex(12)> foo.()
"Hello"
```

関数名の後ろに`.`があることに注意してください。


### Taskの実行

Task.start()で関数を子プロセスで実行できます。
先ほど作成したfoo関数を子プロセスで実行します。

```
iex(19)> task = Task.async(foo)
%Task{owner: #PID<0.80.0>, pid: #PID<0.137.0>, ref: #Reference<0.0.4.1930>}
```

子プロセスの完了を待つにはTask.await()を使います。

```
iex(20)> Task.await(task)
"Hello"
```

実行結果が返されました。

これでは子プロセスが実行されているかわからないので、子プロセスに渡す関数内でProcess.Sleep()するようにします。

```
iex(32)> bar = fn() -> Process.sleep(5000) end
```

bar()を10回実行します。直列に実行すると50秒sleepするはずですが子プロセスで実行されている場合は5〜6秒で完了するはずです。

```
iex(13)> tasks = for n <- 1..10, true, do: Task.async(bar)
[%Task{owner: #PID<0.80.0>, pid: #PID<0.169.0>, ref: #Reference<0.0.1.189>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.170.0>, ref: #Reference<0.0.1.190>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.171.0>, ref: #Reference<0.0.1.191>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.172.0>, ref: #Reference<0.0.1.192>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.173.0>, ref: #Reference<0.0.1.193>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.174.0>, ref: #Reference<0.0.1.194>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.175.0>, ref: #Reference<0.0.1.195>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.176.0>, ref: #Reference<0.0.1.196>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.177.0>, ref: #Reference<0.0.1.197>},
 %Task{owner: #PID<0.80.0>, pid: #PID<0.178.0>, ref: #Reference<0.0.1.198>}]
iex(14)> Task.yield_many(tasks)
[{%Task{owner: #PID<0.80.0>, pid: #PID<0.169.0>, ref: #Reference<0.0.1.189>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.170.0>, ref: #Reference<0.0.1.190>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.171.0>, ref: #Reference<0.0.1.191>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.172.0>, ref: #Reference<0.0.1.192>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.173.0>, ref: #Reference<0.0.1.193>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.174.0>, ref: #Reference<0.0.1.194>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.175.0>, ref: #Reference<0.0.1.195>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.176.0>, ref: #Reference<0.0.1.196>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.177.0>, ref: #Reference<0.0.1.197>},
  {:ok, :ok}},
 {%Task{owner: #PID<0.80.0>, pid: #PID<0.178.0>, ref: #Reference<0.0.1.198>},
  {:ok, :ok}}]
```

yield_many()が5秒強で完了します。

scriptも書いて実行してみます。

delay_task.exs:

```
foo = fn() -> Process.sleep(5000) end
tasks = for _ <- 1..10, true, do: Task.async(foo)
Task.yield_many(tasks)
```

実行します。

```
$ time elixir delay_task.exs
elixir delay_task.exs  0.40s user 0.22s system 11% cpu 5.460 total
```

5.460秒で完了しました。意図している挙動になっていると言えます。
