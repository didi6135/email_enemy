from flask import Blueprint, jsonify

from app.services.repository.suspicious_content_repository import get_all_suspicious_content_by_email

suspicious_content = Blueprint('suspicious_content', __name__)



@suspicious_content.route('/suspicious_content/<email>', methods=['GET'])
def get_suspicious_content_controller(email):
    try:
        all_suspicious_content = get_all_suspicious_content_by_email(email)
        return jsonify({
            'email': email,
            'suspicious_content': all_suspicious_content
        })

    except Exception as e:
        print(f"Error processing message: {e}")
        return jsonify({"error": "An error occurred while processing the message."}), 500