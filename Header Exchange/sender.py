import pika
from pika.exchange_type import ExchangeType

credentials = pika.PlainCredentials('root', 'root')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/myapp',
        credentials=credentials
    )
)
ch = connection.channel()


ch.exchange_declare('he', ExchangeType.headers)
message = 'Hello world..!'

ch.basic_publish(
    exchange='he',
    routing_key='',
    body=message,
    properties=pika.BasicProperties(
        headers={
            'name': 'daryoush'
        }
    )
)
print('Send message')
connection.close()
