import os

from flask import Blueprint, request, jsonify

from app.kafka_setting.producer import producer_send_message
from app.services.producers.message_all_producer.producer import all_messages_producer

all_emails = Blueprint('all_emails', __name__)

@all_emails.route('/api/email', methods=['POST'])
def get_all_emails_controller():
    try:
        data = request.get_data()

        if not data:
            return jsonify({"error": "Invalid data format, JSON expected"}), 400


        future_all_messages = producer_send_message(
            topic=os.environ['KAFKA_TOPIC_ALL_MESSAGES'],
            value=data,
            producer=all_messages_producer
        )



    except Exception as e:
        print(f"Error processing message: {e}")
        return jsonify({"error": "An error occurred while processing the message."}), 500
