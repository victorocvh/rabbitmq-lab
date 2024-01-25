import pika 
from pika import credentials
import sys 

message = ' '.join(sys.argv[1:]) or 'no arg!'
cre = credentials.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cre))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
    routing_key='hello',
    body=message)

print(f" [x] Sent {message} ")

connection.close()