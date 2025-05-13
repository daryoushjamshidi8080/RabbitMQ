
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
ch.exchange_declare(exchange='dlx', exchange_type='fanout')

ch.queue_declare(queue='mainq', arguments={
                 'x-dead-letter-exchange': 'dlx', 'x-message-ttl': 5000, 'x-max-length': 100})

ch.queue_bind(exchange='main', queue='mainq', routing_key='home')


ch.queue_declare(queue='dlxq')
ch.queue_bind('dlxq', 'dlx')


def dlx_callback(ch, method, properties, body):
    print(f'Dead letter : {body}')


ch.basic_consume(queue='dlxq', on_message_callback=dlx_callback, auto_ack=True)

print('Stating Consume')

ch.start_consuming()
