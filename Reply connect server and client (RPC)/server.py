import pika

# Remote Procedure Call
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


def on_request_message_receive(ch, method, properties, body):
    print(
        f'Received request: {body} ------ correlation id : {properties.correlation_id}')

    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id
        ),
        body=f'Reply to {properties.correlation_id}'
    )


print('Staring Server')


ch.queue_declare('request-queue')
ch.basic_consume(queue='request-queue', auto_ack=True,
                 on_message_callback=on_request_message_receive)


ch.start_consuming()
