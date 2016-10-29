# RabbitMQをElixirから利用する

RabbitMQをElixirから利用してみます。
動作環境はOSXを前提にしています。

https://www.rabbitmq.com/tutorials/tutorial-one-elixir.html

## Elixir

```
Elixir (エリクサー) は並列処理の機能や関数型といった特徴を持つ、Erlangの仮想マシン (BEAM) 上で動作するコンピュータプログラミング言語である。
```
Wikipedia より
https://ja.wikipedia.org/wiki/Elixir_(%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E)

なんか良さそう(小並感)。

## RabbitMQ

```
RabbitMQ(ラビットエムキュー)は、Advanced Message Queuing Protocol(AMQP)を使用した、オープンソースのメッセージ指向ミドルウェアである。
```
Wikipediaより
https://ja.wikipedia.org/wiki/RabbitMQ

お世話になっています(小並感)。

## インストール

### Elixirのインストール

homebrewでインストールします。

```
＄brew install elixir
```

インストールが済んだらバージョンを確認してみます。

```
$ elixir -v
Erlang/OTP 19 [erts-8.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]

Elixir 1.3.4
```

## RabbitMQ

### インストールと起動

RabbitMQもhomebrewでインストールします。

```
$ brew install rabbitmq
```

インストールが完了したら起動します。

```
$ rabbitmq-server

              RabbitMQ 3.6.4. Copyright (C) 2007-2016 Pivotal Software, Inc.
  ##  ##      Licensed under the MPL.  See http://www.rabbitmq.com/
  ##  ##
  ##########  Logs: /usr/local/var/log/rabbitmq/rabbit@localhost.log
  ######  ##        /usr/local/var/log/rabbitmq/rabbit@localhost-sasl.log
  ##########
              Starting broker...
 completed with 10 plugins.
```

### RabbitMQの管理画面

RabbitMQには管理画面があります。

http://127.0.0.1:15672/ にアクセスします。

- user: guest
- password: guest

でログインできます。


## Hello World

[RabbitMQのサイト](https://www.rabbitmq.com/tutorials/tutorial-one-elixir.html)に実装例が掲載されているのでそれに従ってやっていきます。
まずは簡単なHello Worldの構成を実装します。

以下が仕様です。

- Producerは"Hello"という文字列をメッセージとして1つRabbitMQにpublishする
- Consumerはメッセージを受け取って標準出力に表示する
- Queueの名前は"hello" とする

簡単ですね?

### mix newでプロジェクトを作成する

mix newでプロジェクトを作成します。プロジェクト名はチュートリアルに従い、rabbitmq_tutorialsにします。

```
$ mix new rabbitmq_tutorials
* creating README.md
* creating .gitignore
* creating mix.exs
* creating config
* creating config/config.exs
* creating lib
* creating lib/rabbitmq_tutorials.ex
* creating test
* creating test/test_helper.exs
* creating test/rabbitmq_tutorials_test.exs

Your Mix project was created successfully.
You can use "mix" to compile it, test it, and more:

    cd rabbitmq_tutorials
    mix test

Run "mix help" for more commands.

```

プロジェクトを作成したら、rabbitmq_tutorialsというディレクトリができています。
以降はプロジェクトディレクトリの中で作業するので、ワーキングディレクトリを移動しておきます。

```
$ cd rabbitmq_tutorials
```

ディレクトリ内にmix.exsというファイルがあります。
mix.exs内には使用するライブラリのバージョンなどを指定できます。
今回はamqpを使うのでそれを指定します。

```
defmodule RabbitmqTutorials.Mixfile do
  use Mix.Project

  def project do
    [app: :rabbitmq_tutorials,
     version: "0.1.0",
     elixir: "~> 1.3",
     build_embedded: Mix.env == :prod,
     start_permanent: Mix.env == :prod,
     deps: deps()]
  end

  def application do
    [applications: [:logger]]
  end

  defp deps do
    [
      {:amqp, "~> 0.1.4"},  # <- これを追加
    ]
  end
end

```

mix.exsを更新したら、mix deps.getとmix deps.compleでライブラリを取得コンパイルします。


mix deps.get:

```
$ mix deps.get
Could not find Hex, which is needed to build dependency :amqp
Shall I install Hex? (if running non-interactively, use: "mix local.hex --force") [Yn] Y
* creating /Users/sximada/.mix/archives/hex-0.13.2
Running dependency resolution
Dependency resolution completed
  amqp: 0.1.5
  amqp_client: 3.5.6
  rabbit_common: 3.5.6
* Getting amqp (Hex package)
  Checking package (https://repo.hex.pm/tarballs/amqp-0.1.5.tar)
  Fetched package
* Getting amqp_client (Hex package)
  Checking package (https://repo.hex.pm/tarballs/amqp_client-3.5.6.tar)
  Fetched package
* Getting rabbit_common (Hex package)
  Checking package (https://repo.hex.pm/tarballs/rabbit_common-3.5.6.tar)
  Fetched package
$
```

良さそうです。

mix deps.compile:

```
$ mix deps.compile
Could not find "rebar", which is needed to build dependency :rabbit_common
I can install a local copy which is just used by Mix
Shall I install rebar? (if running non-interactively, use: "mix local.rebar --force") [Yn] Y
* creating /Users/sximada/.mix/rebar
* creating /Users/sximada/.mix/rebar3
==> rabbit_common (compile)
Compiled src/rabbit_misc.erl
src/gen_server2.erl:770: Warning: random:uniform_s/2: the 'random' module is deprecated; use the 'rand' module instead
src/gen_server2.erl:770: Warning: random:uniform_s/2: the 'random' module is deprecated; use the 'rand' module instead
Compiled src/gen_server2.erl
Compiled src/ssl_compat.erl
Compiled src/time_compat.erl
Compiled src/rabbit_runtime_parameter.erl
Compiled src/rabbit_writer.erl
Compiled src/rabbit_queue_master_locator.erl
Compiled src/rabbit_queue_decorator.erl
Compiled src/rabbit_queue_collector.erl
Compiled src/rabbit_policy_validator.erl
Compiled src/rabbit_password_hashing.erl
src/rabbit_nodes.erl:208: Warning: random:seed/3: the 'random' module is deprecated; use the 'rand' module instead
src/rabbit_nodes.erl:213: Warning: random:uniform/1: the 'random' module is deprecated; use the 'rand' module instead
src/rabbit_nodes.erl:208: Warning: random:seed/3: the 'random' module is deprecated; use the 'rand' module instead
src/rabbit_nodes.erl:213: Warning: random:uniform/1: the 'random' module is deprecated; use the 'rand' module instead
Compiled src/rabbit_nodes.erl
Compiled src/supervisor2.erl
Compiled src/rabbit_networking.erl
Compiled src/rabbit_msg_store_index.erl
Compiled src/rabbit_net.erl
Compiled src/rabbit_reader.erl
Compiled src/rabbit_heartbeat.erl
Compiled src/rabbit_exchange_type.erl
Compiled src/rabbit_exchange_decorator.erl
Compiled src/rabbit_event.erl
Compiled src/rabbit_control_misc.erl
Compiled src/rabbit_command_assembler.erl
Compiled src/rabbit_channel_interceptor.erl
Compiled src/rabbit_framing_amqp_0_9_1.erl
Compiled src/rabbit_binary_parser.erl
Compiled src/rabbit_binary_generator.erl
Compiled src/rabbit_framing_amqp_0_8.erl
Compiled src/rabbit_backing_queue.erl
Compiled src/rabbit_basic.erl
Compiled src/rabbit_authn_backend.erl
Compiled src/rabbit_authz_backend.erl
Compiled src/rabbit_auth_mechanism.erl
Compiled src/priority_queue.erl
Compiled src/pmon.erl
Compiled src/rabbit_channel.erl
Compiled src/mochijson2.erl
Compiled src/mirrored_supervisor.erl
Compiled src/credit_flow.erl
Compiled src/app_utils.erl
Compiled src/rabbit_amqqueue.erl
==> amqp_client (compile)
Compiled src/amqp_gen_consumer.erl
Compiled src/amqp_gen_connection.erl
Compiled src/uri_parser.erl
Compiled src/amqp_sup.erl
Compiled src/rabbit_routing_util.erl
Compiled src/amqp_uri.erl
Compiled src/amqp_rpc_server.erl
Compiled src/amqp_rpc_client.erl
include/amqp_gen_consumer_spec.hrl:30: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:31: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:32: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:34: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:35: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:36: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:37: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:38: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:39: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:42: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:30: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:31: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:32: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:34: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:35: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:36: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:37: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:38: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:39: syntax error before: '/'
include/amqp_gen_consumer_spec.hrl:42: syntax error before: '/'
Compiling src/amqp_selective_consumer.erl failed:
ERROR: compile failed while processing /Users/sximada/ng2/home/src/gist/elixir-tips-rabbmitmq/rabbitmq_tutorials/deps/amqp_client: rebar_abort
** (Mix) Could not compile dependency :amqp_client, "/Users/sximada/.mix/rebar compile skip_deps=true deps_dir="/Users/sximada/ng2/home/src/gist/elixir-tips-rabbmitmq/rabbitmq_tutorials/_build/dev/lib"" command failed. You can recompile this dependency with "mix deps.compile amqp_client", update it with "mix deps.update amqp_client" or clean it with "mix deps.clean amqp_client"
(py3.5.2) $ echo $?
1
```

エラーが出てしまいました。`Could not compile dependency :amqp_client`とあるので:amqp_clientがコンパイルできないようです。再度実行しても同じ結果になります。

stackoverflowに同じ現象の投稿がありました。
http://stackoverflow.com/questions/38207302/how-to-setup-elixir-project-to-use-rabbitmq-via-amqp

どうやらErlang 19でamqpのコンパイルは現状(2016年10月29日現在)できない模様です。
問題はamqp_clientがErlang 19に対応できていないからのようです。
https://github.com/pma/amqp/issues/28

Github上のリポジトリは修正されているようなのでそちらを使うようにmix.exsを変更します。


```
  defp deps do
    [
      {:amqp_client, git: "https://github.com/jbrisbin/amqp_client.git", override: true},  # <- ここを追加
      {:amqp, "~> 0.1.4"},
    ]
  end

```

mix deps.getとmix deps.compileを実行します。

mix deps.get:

```
$ mix deps.get
* Getting amqp_client (https://github.com/jbrisbin/amqp_client.git)
remote: Counting objects: 515, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 515 (delta 0), reused 2 (delta 0), pack-reused 513
Receiving objects: 100% (515/515), 704.25 KiB | 562.00 KiB/s, done.
Resolving deltas: 100% (324/324), done.
* Getting rabbit_common (https://github.com/jbrisbin/rabbit_common.git)
remote: Counting objects: 779, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 779 (delta 0), reused 2 (delta 0), pack-reused 777
Receiving objects: 100% (779/779), 1.16 MiB | 797.00 KiB/s, done.
Resolving deltas: 100% (571/571), done.
fatal: You are on a branch yet to be born
** (Mix) Command "git --git-dir=.git checkout --quiet " failed
```

今度はmix deps.getでエラーしてしまいました。困った。
もう面倒なので直接直してしまいます。

問題のリポジトリはdeps配下にあるので次のようにしました。

```
$ cd deps/rabbit_common
$ git remote update
$ git checkout -b master origin/master
$ cd ../../
$ mix deps.get
```

うーん。
無理矢理直した後のdeps.compile:


```
$ mix deps.compile
==> rabbit_common (compile)
Compiled src/rabbit_authz_backend.erl
src/gen_server2.erl:770: Warning: random:uniform_s/2: the 'random' module is deprecated; use the 'rand' module instead
src/gen_server2.erl:770: Warning: random:uniform_s/2: the 'random' module is deprecated; use the 'rand' module instead
Compiled src/gen_server2.erl
Compiled src/rabbit_authn_backend.erl
Compiled src/ssl_compat.erl
Compiled src/time_compat.erl
Compiled src/rabbit_types.erl
Compiled src/rabbit_runtime_parameter.erl
Compiled src/rabbit_writer.erl
Compiled src/rabbit_queue_master_locator.erl
Compiled src/rabbit_queue_decorator.erl
Compiled src/rabbit_queue_collector.erl
Compiled src/rabbit_policy_validator.erl
Compiled src/rabbit_password_hashing.erl
Compiled src/rabbit_nodes.erl
Compiled src/rabbit_networking.erl
Compiled src/supervisor2.erl
Compiled src/rabbit_msg_store_index.erl
Compiled src/rabbit_heartbeat.erl
Compiled src/rabbit_health_check.erl
Compiled src/rabbit_reader.erl
Compiled src/rabbit_net.erl
Compiled src/rabbit_exchange_type.erl
Compiled src/rabbit_exchange_decorator.erl
Compiled src/rabbit_event.erl
Compiled src/rabbit_error_logger_handler.erl
Compiled src/rabbit_data_coercion.erl
Compiled src/rabbit_ct_helpers.erl
Compiled src/rabbit_framing_amqp_0_9_1.erl
Compiled src/rabbit_control_misc.erl
Compiled src/rabbit_ct_broker_helpers.erl
Compiled src/rabbit_command_assembler.erl
Compiled src/rabbit_channel_interceptor.erl
Compiled src/rabbit_binary_parser.erl
Compiled src/rabbit_framing_amqp_0_8.erl
Compiled src/rabbit_binary_generator.erl
Compiled src/rabbit_backing_queue.erl
Compiled src/rabbit_auth_mechanism.erl
Compiled src/rabbit_basic.erl
Compiled src/rabbit_auth_backend_dummy.erl
Compiled src/rabbit_auth_backend_internal.erl
Compiled src/priority_queue.erl
Compiled src/pmon.erl
Compiled src/mochijson2.erl
Compiled src/rabbit_channel.erl
Compiled src/credit_flow.erl
Compiled src/mirrored_supervisor.erl
Compiled src/code_version.erl
Compiled src/app_utils.erl
Compiled src/rabbit_amqqueue.erl
==> amqp_client (compile)
Compiled src/amqp_gen_consumer.erl
Compiled src/amqp_gen_connection.erl
Compiled src/uri_parser.erl
Compiled src/rabbit_ct_client_helpers.erl
Compiled src/rabbit_routing_util.erl
Compiled src/amqp_sup.erl
Compiled src/amqp_uri.erl
Compiled src/amqp_rpc_server.erl
Compiled src/amqp_selective_consumer.erl
Compiled src/amqp_rpc_client.erl
Compiled src/amqp_direct_consumer.erl
Compiled src/amqp_main_reader.erl
Compiled src/amqp_network_connection.erl
Compiled src/amqp_connection_type_sup.erl
Compiled src/amqp_connection_sup.erl
Compiled src/amqp_client.erl
Compiled src/amqp_direct_connection.erl
Compiled src/amqp_connection.erl
Compiled src/amqp_channel_sup_sup.erl
Compiled src/amqp_channel_sup.erl
Compiled src/amqp_channels_manager.erl
Compiled src/amqp_auth_mechanisms.erl
Compiled src/amqp_channel.erl
==> amqp
Compiling 9 files (.ex)
Generated amqp app
$
```

やったー。でもかなり無理矢理。

### iexでRabbitMQにつないでMessageをpublishする

実際に処理を書く前にインタラクティブモードでライブラリの挙動を確認しておきます。
(別にやんなくてもいいです)

iexを起動します。mixで入れたパッケージを使いたいので-S mixをつけます。

```
$ iex -S mix
Erlang/OTP 19 [erts-8.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]

Compiling 1 file (.ex)
Generated rabbitmq_tutorials app
Interactive Elixir (1.3.4) - press Ctrl+C to exit (type h() ENTER for help)
iex(1)>
```

それでは接続します。

```
iex(2)> {:ok, connection} = AMQP.Connection.open
{:ok, %AMQP.Connection{pid: #PID<0.162.0>}}
iex(3)> {:ok, channel} = AMQP.Channel.open(connection)
{:ok,
 %AMQP.Channel{conn: %AMQP.Connection{pid: #PID<0.162.0>}, pid: #PID<0.172.0>}}

```

接続状況は管理画面から確認できます。
http://127.0.0.1:15672/#/connections

![RabbitMQ管理画面のコネクション状況](https://raw.githubusercontent.com/TakesxiSximada/gist/master/elixir-tips-rabbmitmq/rabbitmq-admin-connection.png)

次にQueueを作成します。AMQP.Queue.declare()を使うと宣言的にQueueを作成できます。

```
iex(4)> AMQP.Queue.declare(channel, "hello")
{:ok, %{consumer_count: 0, message_count: 0, queue: "hello"}}

```

Queueの状況も管理画面から確認できます。
http://127.0.0.1:15672/#/queues

![RabbitMQ管理画面のQueue状況](https://github.com/TakesxiSximada/gist/blob/master/elixir-tips-rabbmitmq/rabbitmq-admin-queue.png)

それではAMQP.Basic.publish()を使ってメッセージをpublishします。

```
iex(6)> AMQP.Basic.publish(channel, "", "hello", "Hello World!")
:ok
```

`hello`はQueue名、`Hello World!`はペイロード、 第二2引数の空文字列はExchangeです。

publishしたメッセージの中身も管理画面から確認できます。
http://127.0.0.1:15672/#/queues/%2F/hello

`Get Message(s)`ボタンを押すと、最初のメッセージを表示します。

![RabbitMQ管理画面のメッセージの確認](https://github.com/TakesxiSximada/gist/blob/master/elixir-tips-rabbmitmq/rabbitmq-admin-message.png)


最後に接続を閉じます。

```
iex(7)> AMQP.Connection.close(connection)
:ok
```

### Producerを実装する

一通りの処理を確認しました。上記のコードを使うことで送信処理を実装できます。

producer.exs:

```
{:ok, connection} = AMQP.Connection.open
{:ok, channel} = AMQP.Channel.open connection
AMQP.Queue.declare(channel, "hello")
status = AMQP.Basic.publish(channel, "", "hello", "Hello World!")
IO.puts status
AMQP.Connection.close connection
```

ではmix runで実行します。

```
$ mix run send.exs
ok
```

管理画面で確認するとQueueに入っているメッセージの個数が増えているのがわかります。

### iexでMessageをconsumeする

引き続きiexでメッセージを取得します。先ほどと同様に接続し、channelとqueueを生成します。

```
iex(1)> {:ok, connection} = AMQP.Connection.open
{:ok, %AMQP.Connection{pid: #PID<0.150.0>}}
iex(2)> {:ok, channel} = AMQP.Channel.open connection
{:ok,
 %AMQP.Channel{conn: %AMQP.Connection{pid: #PID<0.150.0>}, pid: #PID<0.162.0>}}
iex(3)> {:ok, queue} = AMQP.Queue.declare(channel, "hello")
{:ok, %{consumer_count: 0, message_count: 8, queue: "hello"}}
```

次にメッセージを受け取るハンドラを記述します。

```
iex(5)> defmodule Receive do
...(5)>   def wait_for_messages do
...(5)>     receive do
...(5)>       {:basic_deliver, payload, _meta} ->
...(5)>         IO.puts " [x] Received #{payload}"
...(5)>         wait_for_messages
...(5)>     end
...(5)>   end
...(5)> end
{:module, Receive,
 <<70, 79, 82, 49, 0, 0, 6, 188, 66, 69, 65, 77, 69, 120, 68, 99, 0, 0, 0, 140,
   131, 104, 2, 100, 0, 14, 101, 108, 105, 120, 105, 114, 95, 100, 111, 99, 115,
   95, 118, 49, 108, 0, 0, 0, 4, 104, 2, ...>>, {:wait_for_messages, 0}}
```

次の特定のプロセスがqueueからメッセージを取得することを指定します。
sbscribeするqueueが存在するかを確認しておく必要があります。

```
iex(6)> AMQP.Basic.consume(channel, "hello", nil, no_ack: true)
{:ok, "amq.ctag-xrIlXgX1EYFYbvQtgKJUmw"}
```

ハンドラを実行しします。Receive.wait_for_messagesは再帰になっています。

```
iex(7)> Receive.wait_for_messages
 [x] Received Hello World!
 [x] Received Hello World!
 [x] Received Hello World!
 [x] Received Hello World!
 [x] Received Hello World!
 [x] Received Hello World!
 [x] Received Hello World!
 [x] Received Hello World!
```

終了はC-cの後でaです。

### Consumerを実装する

では先ほどのメッセージを受け取る処理をconsumer.exsに実装します。

consumer.exs:

```
{:ok, connection} = AMQP.Connection.open
{:ok, channel} = AMQP.Channel.open connection
{:ok, queue} = AMQP.Queue.declare channel, "hello"

defmodule Receiver do
  def wait_for_messages do
    receive do
      {:basic_deliver, payload, _meta} ->
        IO.puts " [x] Received #{payload}"
        wait_for_messages
    end
  end
end

AMQP.Basic.consume channel, "hello", nil, no_ack: true
Receiver.wait_for_messages
```

consumer.exsを実行します。

```
$ mix run consumer.exs
 [x] Received Hello World!
 [x] Received Hello World!
 [x] Received Hello World!
 [x] Received Hello World!

```

メッセージを取得して処理を行っているのがわかります。
終了はC-cの後でaです。


## 学んだことまとめ

- 外部パッケージのインストールやプロジェクトのスキャフォールディングはmixコマンドを使う
- amqp_clientパッケージは通常のインストール手順で行うとErlang 1.9ではコンパイル
エラーする
- mix.exsのdepsにgitリポジトリを指定するとgitのエラーが出ることがある
  - 今回はdeps配下のリポジトリを手動で直接なおした

- メッセージの送信は次の手順で行う
  1. 接続
  2. channel作成
  3. queue作成
  4. 送信
  5. 切断


- メッセージの受信は次の手順で行う
  1. 接続
  2. channel作成
  3. queue作成
  4. Consumerを実装
  5. subscribeするqueueを指定
  6. 受信開始
