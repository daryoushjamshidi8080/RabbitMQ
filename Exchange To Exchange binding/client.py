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

ch.exchange_declare(exchange='first', exchange_type='direct')
ch.exchange_declare(exchange='secend', exchange_type='fanout')

ch.exchange_bind(destination='secend', source='first')

ch.basic_publish(exchange='first', routing_key='', body='Hello world..!')

print('Send..!')

connection.close()
