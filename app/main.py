from dotenv import load_dotenv
from flask import Flask

from app.kafka_setting.init_topics import init_topics
from app.mongo_setting.config import restart_mongo
from app.postgres_setting.config import reset_database
from app.routes.get_all_email_controller import all_emails
from app.routes.suspicious_content_controller import suspicious_content

load_dotenv(verbose=True)

app = Flask(__name__)

app.register_blueprint(blueprint=all_emails, url_prefix='/api')
app.register_blueprint(blueprint=suspicious_content, url_prefix='/api')

if __name__ == "__main__":
    init_topics()
    reset_database()
    restart_mongo()
    app.run()


