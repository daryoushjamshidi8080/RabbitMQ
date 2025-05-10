import pika
import uuid


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

reply_queue = ch.queue_declare(queue='', exclusive=True)


def on_reply_message_receive(ch, method, properties, body):
    print(f'reply receive {body}')


ch.basic_consume(queue=reply_queue.method.queue, auto_ack=True,
                 on_message_callback=on_reply_message_receive)


ch.queue_declare(queue='request-queue')

cor_id = str(uuid.uuid4())

print(f'Sending Request: {cor_id}')

ch.basic_publish(
    exchange='',
    routing_key='request-queue',
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    ),
    body='Can i request a reply?'
)

print('Starting Client')

ch.start_consuming()
