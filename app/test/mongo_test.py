import pytest
from pymongo import MongoClient


@pytest.fixture(scope="module")
def mongo_client():

    client = MongoClient("mongodb://172.23.14.159:27017")
    test_db = client["test_email_enemy"]
    yield test_db
    client.drop_database("test_email_enemy")

@pytest.fixture
def sample_data():
    return {
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
            "Public quickly spend hear sing.",
            "Difference nothing environmental shake decide.",
            "Natural southern what nice."
        ]
    }


def test_insert_message(mongo_client, sample_data):
    result = mongo_client["all_messages"].insert_one(sample_data)
    assert result.inserted_id is not None

    stored_data = mongo_client["all_messages"].find_one({"email": "jeremy37@example.org"})
    assert stored_data is not None
    assert stored_data["username"] == "jonesalejandra"
    assert stored_data["location"]["city"] == "Port Josephburgh"

