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


ch.exchange_declare(exchange='alt', exchange_type='fanout')
ch.exchange_declare(exchange='main', exchange_type='direct',
                    arguments={'alternate-exchange': 'alt'})


ch.queue_declare(queue='altq')
ch.queue_bind(queue='altq', exchange='alt')

ch.queue_declare(queue='mainq')
ch.queue_bind(queue='mainq', exchange='main', routing_key='home')


def alt_callback(ch, method, properties, body):
    with open('altExchg.log', 'a') as file:
        file.write(f'time: {datetime.now()}  Alt: {body.decode()}\n')


def main_callback(ch, method, properties, body):
    print(f' Main : {body} ')


ch.basic_consume(queue='altq', on_message_callback=alt_callback, auto_ack=True)
ch.basic_consume(
    queue='mainq', on_message_callback=main_callback, auto_ack=True)

print('Start Consuming.. !')

ch.start_consuming()
