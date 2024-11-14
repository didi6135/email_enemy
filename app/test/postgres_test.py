import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import UserDetail, Location, DeviceInfo, ExplosiveSentence, HostageSentence, Base


load_dotenv(verbose=True)

engine = create_engine(os.environ['TEST_POSTGRES_URL'])
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def sample_user_data():
    return UserDetail(
        email="jeremy37@example.org",
        username="jonesalejandra",
        ip_address="215.67.111.124",
        location=Location(latitude=8.5478895, longitude=-135.24204, city="Port Josephburgh", country="PA"),
        device=DeviceInfo(browser="Mozilla/5.0", os="iOS", device_id="c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81")
    )


def test_insert_user(db_session, sample_user_data):
    db_session.add(sample_user_data)
    db_session.commit()

    user = db_session.query(UserDetail).filter_by(email="jeremy37@example.org").first()
    assert user is not None
    assert user.username == "jonesalejandra"
    assert user.location.city == "Port Josephburgh"
    assert user.device.device_id == "c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81"



def test_get_suspicious_content_by_email(db_session, sample_user_data):
    sample_user_data.explosive_sentences = [ExplosiveSentence(content="Sample explosive sentence")]
    sample_user_data.hostage_sentences = [HostageSentence(content="Sample hostage sentence")]
    db_session.add(sample_user_data)
    db_session.commit()

    user = db_session.query(UserDetail).filter_by(email="jeremy37@example.org").first()
    assert user is not None
    assert len(user.explosive_sentences) == 1
    assert len(user.hostage_sentences) == 1
    assert user.explosive_sentences[0].content == "Sample explosive sentence"
    assert user.hostage_sentences[0].content == "Sample hostage sentence"