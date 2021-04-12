import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import io
import pandas as pd

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
            conn=self.connect()
            df = pd.read_csv("./testfilecsv.csv")
            df.head(0).to_sql('resource', conn, if_exists='replace',index=False) #drops old table and creates new empty table
            cur = conn.cursor()
            output = io.StringIO()
            df.to_csv(output, sep='\t', header=False, index=False)
            output.seek(0)
            contents = output.getvalue()
            cur.copy_from(output, 'resource', null="") # null values become ''
            conn.commit()
            # conn = self.connect()
            # cursor = conn.cursor()
            # my_file = open("./testfilecsv.csv")
            # sql = "COPY resource(subscriptionname,date, servicename,serviceresource, quantity, cost) FROM testfilecsv DELIMITER ',' CSV header;"
            # cursor.copy_expert(sql, my_file)

            # f = open('testfilecsv.csv', 'r')
            # with open('testfilecsv.csv', 'r') as f:
                # cursor.copy_from(f, 'resource', columns=(
                #     'subscriptionname,date, servicename,serviceresource, quantity, cost'))
                # cursor.copy_expert("COPY test TO RESOURCE", "testfilecsv.csv")
            # conn.commit()
            # f.close()
        except (Exception, Error) as error:
            print("Error trying adding data", error)


data = Send_Data()
data.add_data()
