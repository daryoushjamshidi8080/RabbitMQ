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

ch.basic_publish(exchange='logs', routing_key='', body='FANOUT..!')

print('Message Send.')

connection.close()
