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


message = {
    'error.warning.important': 'This is an important message',
    'info.debug.notimportant': 'This is not an important message'
}

for k, v in message.items():
    ch.basic_publish('topic_logs', routing_key=k, body=v)

print('Send message..')
connection.close()
