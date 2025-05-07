import pika
import time


credentials = pika.PlainCredentials('root', 'root')


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/myapp',
        credentials=credentials
    ))
ch = connection.channel()
ch.queue_declare(queue='one')

ch.basic_publish(
    exchange='',
    routing_key='one',
    body='Hello World ...',
    properties=pika.BasicProperties(
        content_type='text/plain',
        content_encoding='gzip',
        timestamp=int(time.time()),
        expiration='60000000',
        delivery_mode=2,
        # user_id='10',
        app_id='25',
        type='exch.queue',
        headers={'name': 'daryoush', 'age': '30'}
    )
)

print('message sent..!')
connection.close()
