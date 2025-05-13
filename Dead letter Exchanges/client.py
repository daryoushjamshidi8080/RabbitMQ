import pika
from datetime import datetime

credentials = pika.PlainCredentials('root', 'root')


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/myapp',
        credentials=credentials
    ))
ch = connection.channel()

ch.exchange_declare(exchange='main', exchange_type='direct')
ch.basic_publish(exchange='main', routing_key='home', body='Hello World')

print('Send ..!')

connection.close()
