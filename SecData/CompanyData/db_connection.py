import psycopg2
from psycopg2.extras import execute_batch
from dotenv import load_dotenv
import os

class DbConnections:

    def __init__(self, name):
        self.env_path = os.path.join(os.path.dirname(__file__), '.env')
        self.db_name = name

        try:
            load_dotenv(self.env_path)
            self.conn = psycopg2.connect('dbname=' + self.db_name
                                        + ' user=' + os.environ.get('db_user')
                                        + ' host=' + os.environ.get('db_host')
                                        + ' password=' + os.environ.get('db_password'))
            print("Successfully connected to the database.")
        except:
            print("I am unable to connect to the database")

    def write_data(self, table, data=[]):
        cursor = self.conn.cursor()
        sqlStatement = """INSERT INTO {} VALUES (%s, %s) ON CONFLICT DO NOTHING""".format(table)
        execute_batch(cursor, sqlStatement, data)
        self.conn.commit()

