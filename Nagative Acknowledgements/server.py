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

ch.exchange_declare(exchange='aj', exchange_type='fanout')
ch.queue_declare(queue='main')
ch.queue_bind('main', 'aj')


def callback(ch, method, properties, body):
    if method.delivery_tag % 5 == 0:
        ch.basic_nack(delivery_tag=method.delivery_tag,
                      requeue=False, multiple=True)
    print(f' Reseive : {method.delivery_tag}')


ch.basic_consume(queue='main', on_message_callback=callback)
print('starting consume..!')
ch.start_consuming()
