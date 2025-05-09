import pika
from pika.exchange_type import ExchangeType


credentials = pika.PlainCredentials('root', 'root')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='local'))
ch = connection.channel()


ch.exchange_declare('he', ExchangeType.headers)
