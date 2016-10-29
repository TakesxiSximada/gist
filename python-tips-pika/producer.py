#! /usr/bin/env python
import json
import pika


conn_params = pika.ConnectionParameters(host='127.0.0.1')
conn = pika.BlockingConnection(conn_params)

channel = conn.channel()

properties = pika.BasicProperties(content_type='application/json')

channel.basic_publish(
    routing_key='test',
    exchange='test_exchange',
    body=json.dumps({'test': 'ok'}),
    properties=properties,
)

conn.close()
