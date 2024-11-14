from flask import Blueprint, request, jsonify

from app.services.check_messages_service import check_sentences_for_explosive_or_hostage
from app.services.producers.all_messages_producer import send_data_to_all_messages_consumer
from app.services.producers.message_explosive_producer import send_data_to_messages_explosive_consumer
from app.services.producers.message_hostage_producer import send_data_to_messages_hostage_consumer

all_emails = Blueprint('all_emails', __name__)

@all_emails.route('/email', methods=['POST'])
def get_all_emails_controller():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid data format, JSON expected"}), 400


        send_data_to_all_messages_consumer(data)

        keyword = check_sentences_for_explosive_or_hostage(data.get("sentences", []))
        if keyword == "explosive":
            send_data_to_messages_explosive_consumer(data)
        elif keyword == "hostage":
            send_data_to_messages_hostage_consumer(data)

        return jsonify({"status": "Message processed successfully."}), 200


    except Exception as e:
        print(f"Error processing message: {e}")
        return jsonify({"error": "An error occurred while processing the message."}), 500
