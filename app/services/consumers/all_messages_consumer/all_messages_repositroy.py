from app.mongo_setting.config import all_messages_collection


def insert_new_email_message(email_message):
    try:
        result = all_messages_collection.insert_one(email_message)
        print(f"New email message added with ID: {result.inserted_id}")
        return result.inserted_id
    except Exception as e:
        print(f"Error inserting new email message: {e}")
        return None