import pika
from pika.exchange_type import ExchangeType


credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='local'))
ch = connection.channel()


ch.exchange_declare('he', ExchangeType.headers)
ch.queue_declare('hq-any')


bind_args = {'x-match': 'any', 'name': 'daryoush', 'age': '24'}


def callback(ch, method, properties, body):
    print(body)


ch.queue_bind(exchange='he', queue='hq-any', arguments=bind_args)
ch.basic_consume(queue='hq-any', on_message_callback=callback, auto_ack=True)


ch.start_consuming()
