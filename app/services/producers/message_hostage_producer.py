import os
from dotenv import load_dotenv

from app.kafka_setting.producer import create_producer, producer_send_message


load_dotenv(verbose=True)

message_hostage_producer = create_producer()


def send_data_to_messages_hostage_consumer(data):
    try:
        producer_send_message(
            topic=os.environ['KAFKA_TOPIC_HOSTAGE'],
            value=data,
            producer=message_hostage_producer
        )
        print("Data sent successfully.")

    except Exception as e:
        print(f"Error sending data to Kafka: {e}")

