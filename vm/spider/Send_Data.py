import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")


class Send_Data:
    def __init__(self):
        self.host = os.getenv("PSQL_HOST")
        self.db_name = os.getenv("PSQL_DATABASE")
        self.user = os.getenv("PSQL_USER")
        self.password = os.getenv("PSQL_PASS")

    def connect(self):
        # Construct connection string
        try:
            # Connect to an existing database
            connection = psycopg2.connect(user=self.user, password=self.password,
                                          host=self.host, port="5432", database=self.db_name, sslmode='require')
            # Create a cursor to perform database operations
            #cursor = connection.cursor()

            # Print PostgreSQL details
            print("Connected to the database")
            return connection
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def add_data(self):
        try:
            with open('******.csv', 'r') as f:
                conn = self.connect()
                cursor = conn.cursor()
                cursor.copy_from()
                f = open('file.csv', 'r')
                cursor.copy_from(f, 'resource', sep=',', columns=(
                    'subscriptionname,date, servicename,serviceresource, quantity, cost'))
                f.close()
        except (Exception, Error) as error:
            print("Error trying adding data", error)


data = Send_Data()
data.connect()
