import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
ch = connection.channel()


ch.queue_declare(queue='one')


ch.basic_publish(exchange='', routing_key='one', body='Hello World ...')
print('message send..!')
connection.close()
