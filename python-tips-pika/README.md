# [Python][RabbitMQ][Pika] Rabbitmq + Pika(Python) でmessage queueを使う

## AMQPとは

Messsage Queueのためのプロトコルの一つです。

## 仕様

### Producer (Publisher)

メッセージをキューイングします。

### Comsumer (Subscriber)

キューイング済みのメッセージをブローカーから取得します。

### Broker

キューイングされたメッセージを保持し、コンシューマーに渡します。

### Queue

メッセージをためます。

### Exchange

メッセージのルーティングの方式です。

## Rabbitmqとは

AMQPミドルウェアです。AMQPでメッセージを登録したり取り出したりできます。

https://www.rabbitmq.com/

## Pikaとは

Pythonで記述されたAMQPのライブラリです。

https://pika.readthedocs.io/

### Consumer

メッセージを受け取ったら標準出力に表示してACKするコンシューマを作ります。

1. AMQPサーバに接続する

   ```
   >>> import pika

   >>> conn_param = pika.ConnectionParameters(host='127.0.0.1')
   >>> conn = pika.BlockingConnection(conn_param)
   ```

2. channelを生成し設定する

   ここではQoSの設定をしています。

   ```
   >>> channel = conn.channel()
   >>> channel.basic_qos(prefetch_count=1)

   ```

3. メッセージハンドラを定義してchannelに登録する

   `on_message` というハンドラを作成してcallbackとして登録します。
   `basic_consume()` の第二引数はrouting keyです。

   ```
   >>> def on_message(channel, method_frame, header_frame, body):
   ...    print(channel, method_frame, header_frame, body)
   ...    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
   ...
   >>> channel.basic_consume(on_message, 'test')
   ```

4. consumeを始める

   `channel.start_consuming()` でメッセージの受け取りを開始しています。
   受け取ったメッセージはメッセージハンドラに引数として渡され呼び出されます。
   使い終わったコネクションオブジェクを閉じます。

   ```
   >>> try:
   ...    channel.start_consuming()
   ... except Exception as err:
   ...    channel.stop_consuming()
   ...
   >>> conn.close()
   ```

コンシューマを実行した後でrabbitmqの管理画面からメッセージをキューに登録すると、
コンシューマがメッセージを受け取ります。

### Producer

メッセージを1つpublishします。

1. AMQPサーバに接続する

   ```
   >>> conn_params = pika.ConnectionParameters(host='127.0.0.1')
   >>> conn = pika.BlockingConnection(conn_params)
   ```

2. channelを作成する

   ```
   >>> channel = conn.channel()
   ```

3. メッセージをpublishする

   `pika.BasicProperties()` でメッセージに付加する属性を作成しています。
   `content_type='application/json'` なのでメッセージのbodyはJSON形式だということを表しています。

   ```
   >>> properties = pika.BasicProperties(content_type='application/json')
   ```

   `channel.basic_publish()` でメッセージをpublishしています。

   ```
   >>> channel.basic_publish(
   ...     routing_key='test',
   ...     exchange='test_exchange',
   ...     body=json.dumps({'test': 'ok'}),
   ...     properties=properties,
   ... )

   ```

   最後に接続を閉じます。

   ```
   >>> conn.close()
   ```
