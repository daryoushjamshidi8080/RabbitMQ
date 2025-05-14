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
ch.exchange_declare('aj', exchange_type='fanout')

while True:
    ch.basic_publish(exchange='aj', routing_key='home', body='hello world..!')
    print(' Send ..!')
    input('press any key to continue..!')
