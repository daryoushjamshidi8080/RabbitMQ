import pika


credentials = pika.PlainCredentials('logg', 'log')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='hosts',
        credentials=credentials
    )
)
ch = connection.channel()
ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

result_exchange = ch.queue_declare(queue='', exclusive=True)

ch.queue_bind(exchange='topic_logs',
              queue=result_exchange.method.queue, routing_key='error.warning.important')

print('Waiting for messages.. ')


def callback(ch, method, properties, body):
    print(body)


ch.basic_consume(queue=result_exchange.method.queue,
                 on_message_callback=callback, auto_ack=True)
ch.start_consuming()
