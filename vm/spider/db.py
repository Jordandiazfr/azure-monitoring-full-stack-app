import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv
from os.path import join, dirname
load_dotenv()

class PostGreSQL:
    def __init__(self):
        self.host = os.environ.get('PSQL_HOST')
        self.db_name = os.environ.get('PSQL_DATABASE')
        self.user = os.environ.get('PSQL_USER')
        self.password = os.environ.get('PSQL_PASS')
        self.sslmode = "require"
        self.port = "5432"


    def connect(self):
        # Construct connection string
        try:
            # Connect to an existing database
            connection = psycopg2.connect(user=self.user, password=self.password,
                                          host=self.host, port=self.port, database=self.db_name, sslmode=self.sslmode)

            # Create a cursor to perform database operations
            cursor = connection.cursor()

            # Print PostgreSQL details
            print("Connected to the database")
            return connection
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def create_table(self, table_name: str):
        conn = self.connect()
        cursor = conn.cursor()
        SQL_QUERY = """CREATE TABLE IF NOT EXISTS {0} (
            id_cours SERIAL PRIMARY KEY,
            title VARCHAR(250) UNIQUE) ;""".format(table_name)
        cursor.execute(SQL_QUERY)
        conn.commit()
        cursor.close()
        conn.close()
        print("Table " + table_name + " created")

    def select(self, table):
        conn = self.connect()
        cursor = conn.cursor()
        # Fetch all rows from table
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        # Print all rows
        cursor.close()
        conn.close()
        return rows

    def insert(self, table, data: list):
        conn = self.connect()
        c = conn.cursor()
        if data != "":
            query = """INSERT INTO %s (title) VALUES (%s);""" % (
                table, data)
            #new_data = data
            c.execute(query)
            conn.commit()
            c.close()
            conn.close()

    def drop(self):
        pass

    def exec(self, query):
        conn = self.connect()
        c = conn.cursor(dictionary=True)
        c.execute(query)
        # Store + print the fetched data
        result = c.fetchall()
        # Remember to save + close
        conn.commit()
        c.close()
        conn.close()

        return result
    
if __name__ == "__main__":
    p = PostGreSQL()
    result = p.select("resource")
    print(result)