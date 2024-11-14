from dotenv import load_dotenv
from flask import Flask


from app.routes.get_all_email_controller import all_emails
from app.routes.suspicious_content_controller import suspicious_content

load_dotenv()

app = Flask(__name__)

app.register_blueprint(blueprint=all_emails, url_prefix='/api')
app.register_blueprint(blueprint=suspicious_content, url_prefix='/api')

if __name__ == "__main__":
    # init_topics()
    # reset_database()
    # restart_mongo()
    app.run()


