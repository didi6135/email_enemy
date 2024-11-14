import os

from flask import Flask
from kafka.errors import KafkaError

from app.kafka_setting.consumer import create_consumer
from app.services.consumers.message_explosive_consumer.message_explosive_repository import insert_all_data_explosive
from app.services.sentences_service import organize_sentences

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
                fix_data = organize_sentences(message.value)

                user_detail_id = insert_all_data_explosive(fix_data)
                print(user_detail_id)
        except KafkaError as e:
            print(f"Error while consuming messages: {e}")



if __name__ == '__main__':
    consume_messages(new_consumer)
    app.run()
