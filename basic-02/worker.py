import pika 
import sys, os 
from pika import credentials
import time 

def main():
    cre = credentials.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cre))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        
        # Simulating time-consuming task.
        time.sleep(body.count(b'.'))
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello',
        auto_ack=True,
        on_message_callback=callback)

    print(f" [*] Waiting for messages. To exit press CTRL + C")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

