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

ch.exchange_declare(exchange='logs', exchange_type='fanout')
result_queue = ch.queue_declare(queue='', exclusive=True)
ch.queue_bind(exchange='logs', queue=result_queue.method.queue)

print('Waiting for logs.. ')
print(f'queue name : {result_queue.method.queue}')


def callback(ch, method, properties, body):
    print(f'message : {body}')


ch.basic_consume(queue=result_queue.method.queue,
                 on_message_callback=callback, auto_ack=True)


ch.start_consuming()
