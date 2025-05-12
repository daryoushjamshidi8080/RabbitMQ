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


ch.exchange_declare(exchange='alt', exchange_type='fanout')
ch.exchange_declare(exchange='main', exchange_type='direct',
                    arguments={'alternate-exchange': 'alt'})


ch.basic_publish(exchange='main', routing_key='home',
                 body='helle from daryoush')
print('Send message ..!')

connection.close()
