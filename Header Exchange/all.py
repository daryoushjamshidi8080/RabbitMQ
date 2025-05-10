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
ch.queue_declare(queue='hq-all')
bind_args = {'x-match': 'all', 'name': 'daryoush', 'age': 26}

ch.queue_bind(queue='hq-all', exchange='he', arguments=bind_args)


def callback(ch, method, properties, body):
    print(body)


print('Waiting message')

ch.basic_consume(queue='hq-all', on_message_callback=callback, auto_ack=True)
ch.start_consuming()
