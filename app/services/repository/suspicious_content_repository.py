from collections import Counter

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from app.models import UserDetail, ExplosiveSentence, HostageSentence
from app.postgres_setting.config import session_maker
from app.services.sentences_service import organize_sentences


def format_sentences(sentences, sentence_type):
    return [
        {
            "content": sentence.content.splitlines(),
            "created_at": sentence.created_at.strftime('%a, %d %b %Y %H:%M:%S GMT')
        }
        for sentence in sentences
    ]

def get_device_info(device):
    if not device:
        return None
    return {
        "browser": device.browser,
        "os": device.os,
        "device_id": device.device_id
    }

def get_location_info(location):
    if not location:
        return None
    return {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "city": location.city,
        "country": location.country
    }

def get_detailed_suspicious_content_by_email(email):
    with session_maker() as session:
        # Fetch user with joined tables
        user_data = (
            session.query(UserDetail)
            .options(
                joinedload(UserDetail.explosive_sentences),
                joinedload(UserDetail.hostage_sentences),
                joinedload(UserDetail.device),
                joinedload(UserDetail.location)
            )
            .filter(UserDetail.email == email)
            .first()
        )

        if not user_data:
            return {"error": "User not found"}

        # Construct suspicious content, device info, and location details
        suspicious_content = {
            "explosive_sentences": format_sentences(user_data.explosive_sentences, "explosive"),
            "hostage_sentences": format_sentences(user_data.hostage_sentences, "hostage")
        }
        device_info = get_device_info(user_data.device)
        location_info = get_location_info(user_data.location)

        return {
            "email": email,
            "device_info": device_info,
            "location": location_info,
            "suspicious_content": suspicious_content
        }

# Example usage
print(get_detailed_suspicious_content_by_email('wolfescott@example.net'))



def get_most_common_word_in_each_type_of_sentences():
    try:
        with session_maker() as session:
            explosive_sentences = session.query(ExplosiveSentence.content).all()
            hostage_sentences = session.query(HostageSentence.content).all()


            all_sentences = [sentence.content for sentence in explosive_sentences] + \
                            [sentence.content for sentence in hostage_sentences]

            all_text = " ".join(all_sentences).lower().split()
            most_common_word = Counter(all_text).most_common(1)

            return {
                "most_common_word": most_common_word[0] if most_common_word else None
            }

    except SQLAlchemyError as e:
        print(f"An error occurred while inserting all data: {e}")
        return None


print(get_most_common_word_in_each_type_of_sentences())