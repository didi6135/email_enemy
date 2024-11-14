from dotenv import load_dotenv
from flask import Flask

from app.mongo_setting.config import restart_mongo
from app.postgres_setting.config import reset_database
from app.routes.get_all_email_controller import all_emails

# Load environment variables
load_dotenv()

app = Flask(__name__)

app.register_blueprint(blueprint=all_emails)

if __name__ == "__main__":
    # init_topics()
    reset_database()
    restart_mongo()
    app.run()


