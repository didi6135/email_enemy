from sqlalchemy.exc import SQLAlchemyError

from app.models import DeviceInfo, UserDetail, ExplosiveSentence, HostageSentence
from app.models.location import Location
from app.postgres_setting.config import session_maker


data = {
  "email": "jeremy37@example.org",
  "username": "jonesalejandra",
  "ip_address": "215.67.111.124",
  "created_at": "2024-10-15T05:29:13.450066",
  "location": {
      "latitude": 8.5478895,
      "longitude": -135.24204,
      "city": "Port Josephburgh",
      "country": "PA"
  },
  "device_info": {
      "browser": "Mozilla/5.0",
      "os": "iOS",
      "device_id": "c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81"
  },
  "sentences": [
      "explosive quickly spend hear sing.",
      "Difference nothing environmental shake decide.",
      "Natural southern what nice."
  ]
}

def insert_location(location_data):
    try:
        with session_maker() as session:
            location = Location(
                latitude=location_data["latitude"],
                longitude=location_data["longitude"],
                city=location_data["city"],
                country=location_data["country"]
            )
            session.add(location)
            session.commit()
            session.refresh(location)
            return location.id
    except SQLAlchemyError as e:
        print(f"An error occurred while inserting location: {e}")
        return None

def insert_device_info(device_info_data):
    try:
        with session_maker() as session:
            device_info = DeviceInfo(
                browser=device_info_data["browser"],
                os=device_info_data["os"],
                device_id=device_info_data["device_id"]
            )
            session.add(device_info)
            session.commit()
            session.refresh(device_info)
            return device_info.id
    except SQLAlchemyError as e:
        print(f"An error occurred while inserting device info: {e}")
        return None


def insert_user_detail(user_data, location_id, device_id):
    try:
        with session_maker() as session:
            user_detail = UserDetail(
                email=user_data["email"],
                username=user_data["username"],
                ip_address=user_data["ip_address"],
                location_id=location_id,
                device_id=device_id
            )
            session.add(user_detail)
            session.commit()
            session.refresh(user_detail)
            return user_detail.id
    except SQLAlchemyError as e:
        print(f"An error occurred while inserting user detail: {e}")
        return None


def insert_hostage_sentence(user_detail_id, sentences):
    try:
        with session_maker() as session:
            content = " ".join(sentences)
            hostage_sentence = HostageSentence(
                user_detail_id=user_detail_id,
                content=content
            )
            session.add(hostage_sentence)
            session.commit()
            return hostage_sentence.id
    except SQLAlchemyError as e:
        print(f"An error occurred while inserting hostage sentence: {e}")
        return None


def insert_all_data_hostage(data):
    try:
        location_id = insert_location(data['location'])
        device_id = insert_device_info(data['device_info'])

        if location_id is None or device_id is None:
            print("Failed to insert location or device info; aborting.")
            return None

        user_detail_id = insert_user_detail(data, location_id, device_id)

        if user_detail_id is None:
            print("Failed to insert user detail; aborting.")
            return None

        insert_hostage_sentence(user_detail_id, data['sentences'])
        print("Data inserted successfully.")
        return user_detail_id


    except SQLAlchemyError as e:
        print(f"An error occurred while inserting all data: {e}")
        return None


