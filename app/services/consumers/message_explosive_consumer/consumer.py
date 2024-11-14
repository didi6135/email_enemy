import os

from flask import Flask
from kafka.errors import KafkaError

from app.kafka_setting.consumer import create_consumer
from app.services.consumers.all_messages_consumer.all_messages_repositroy import insert_new_email_message

app = Flask(__name__)

new_consumer = create_consumer(
    topic=os.environ['KAFKA_TOPIC_EXPLOSIVE'],
    bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
)


def consume_messages(consumer):
    if consumer:
        print("Listening for messages...")
        try:
            for message in consumer:
                print(f"New message: {message.value}")
                user_id = insert_new_email_message(message.value)
                print(user_id)
        except KafkaError as e:
            print(f"Error while consuming messages: {e}")



if __name__ == '__main__':
    consume_messages(new_consumer)
    app.run()
