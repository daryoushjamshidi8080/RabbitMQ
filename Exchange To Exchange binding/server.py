import pika


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
ch.exchange_declare(exchange='secend', exchange_type='fanout')
ch.queue_declare(queue='daryoush')
ch.queue_bind(queue='daryoush', exchange='secend')


def callback(ch, method, properties, body):
    print(body)


ch.basic_consume(queue='daryoush', auto_ack=True, on_message_callback=callback)
print('Start Consuming..!')
ch.start_consuming()
