from dotenv import load_dotenv
from flask import Flask

from app.kafka_setting.init_topics import init_topics
from app.routes.get_all_email_controller import all_emails

# Load environment variables
load_dotenv()

app = Flask(__name__)

app.register_blueprint(blueprint=all_emails)

if __name__ == "__main__":
    init_topics()
    app.run()

