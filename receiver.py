import pika

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


def callback(ch, method, properties, body):
    print(f'Receinved  : {body}')


ch.basic_consume(queue='one', on_message_callback=callback, auto_ack=True)
print('Waiting for message, to exit press ctrl+c')
ch.start_consuming()
