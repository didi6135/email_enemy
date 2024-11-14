import os

from dotenv import load_dotenv

from app.kafka_setting.producer import create_producer, producer_send_message


load_dotenv(verbose=True)

all_messages_producer = create_producer()


def send_data_to_all_messages_consumer(data):
    try:
        producer_send_message(
            topic=os.environ['KAFKA_TOPIC_ALL_MESSAGES'],
            value=data,
            producer=all_messages_producer
        )
        print("Data sent successfully.")

    except Exception as e:
        print(f"Error sending data to Kafka: {e}")

