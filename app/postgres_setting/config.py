import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import  sessionmaker
from dotenv import load_dotenv

from app.models import Base

load_dotenv()

POSTGRES_URL = os.getenv('POSTGRES_URL')
engine = create_engine(POSTGRES_URL)
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def reset_database():
    try:
        engine = session_maker().bind
        print("Dropping all tables...")
        Base.metadata.drop_all(bind=engine)

        print("Creating all tables...")
        Base.metadata.create_all(bind=engine)

        print("Database reset successfully: all tables dropped and recreated.")
    except SQLAlchemyError as e:
        print(f"An error occurred while resetting the database: {e}")