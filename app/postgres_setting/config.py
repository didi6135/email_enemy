from contextlib import contextmanager
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv(verbose=True)

POSTGRES_URL = os.getenv('POSTGRES_URL')


def get_db_connection():
    return psycopg2.connect(POSTGRES_URL, cursor_factory=RealDictCursor)

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS locations (
        id SERIAL PRIMARY KEY,
        latitude FLOAT,
        longitude FLOAT,
        city VARCHAR(100),
        country VARCHAR(2)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS device_info (
        id SERIAL PRIMARY KEY,
        browser VARCHAR(255),
        os VARCHAR(50),
        device_id VARCHAR(255) UNIQUE
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emails (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        username VARCHAR(100),
        ip_address VARCHAR(15),
        created_at TIMESTAMP,
        location_id INT REFERENCES locations(id) ON DELETE SET NULL,
        device_id INT REFERENCES device_info(id) ON DELETE SET NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sentences (
        id SERIAL PRIMARY KEY,
        email_id INT REFERENCES emails(id) ON DELETE CASCADE,
        content TEXT
    );
    ''')

    connection.commit()
    cursor.close()
    connection.close()
    print("Tables created successfully.")



def drop_all_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS locations;
        DROP TABLE IF EXISTS device_info;
        DROP TABLE IF EXISTS emails;
        DROP TABLE IF EXISTS sentences;
    ''')

    connection.commit()
    cursor.close()
    connection.close()



@contextmanager
def db_connection():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"An error occurred: {e}")
        raise e
    finally:
        cursor.close()
        connection.close()