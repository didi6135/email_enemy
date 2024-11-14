from flask import Blueprint, jsonify

from app.services.repository.suspicious_content_repository import get_detailed_suspicious_content_by_email, \
    get_most_common_word_in_each_type_of_sentences

suspicious_content = Blueprint('suspicious_content', __name__)



@suspicious_content.route('/suspicious_content/<email>', methods=['GET'])
def get_suspicious_content_controller(email):
    try:
        all_suspicious_content = get_detailed_suspicious_content_by_email(email)
        return jsonify(all_suspicious_content)

    except Exception as e:
        print(f"Error processing message: {e}")
        return jsonify({"error": "An error occurred while processing the message."}), 500



@suspicious_content.route('/most_common_word', methods=['GET'])
def get_most_common_word_controller():
    try:
        get_most_comment_word = get_most_common_word_in_each_type_of_sentences()
        return jsonify(get_most_comment_word)
    except Exception as e:
        print(f"Error processing message: {e}")
        return jsonify({"error": "An error occurred while processing the message."}), 500