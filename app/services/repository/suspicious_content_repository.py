from app.postgres_setting.config import session_maker


def get_all_suspicious_content_by_email(email):
    with session_maker() as session:
        user_data = (

        )