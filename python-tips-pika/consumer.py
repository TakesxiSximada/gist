#! /usr/bin/env python
import pika

conn_param = pika.ConnectionParameters(host='127.0.0.1')
conn = pika.BlockingConnection(conn_param)

channel = conn.channel()


def on_message(channel, method_frame, header_frame, body):
    print(channel, method_frame, header_frame, body)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message, 'test')

try:
    channel.start_consuming()
except Exception as err:
    print(err)
    channel.stop_consuming()

conn.close()
