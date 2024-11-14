import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)

client = MongoClient(os.environ['MONGO_URL'])
db = client['email_enemy']

def restart_mongo():
    db.drop_collection('all_messages')


    db.create_collection('all_messages')
    print("Database reset: all collections dropped and recreated.")
