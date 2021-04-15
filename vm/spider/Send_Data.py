import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import pandas as pd

load_dotenv(dotenv_path="./.env")


class Send_Data:
    def __init__(self):
        self.host = os.getenv("PSQL_HOST")
        self.db_name = os.getenv("PSQL_DATABASE")
        self.user = os.getenv("PSQL_USER")
        self.password = os.getenv("PSQL_PASS")
        self.data_list = self.add_data()
        self.conn = self.connect()

    def connect(self):
        try:
            conn = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host, port="5432",
                database=self.db_name,
                sslmode='require'
            )
            print("Connected to the database")
            return conn
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def add_data(self):
        try:
            SubscriptionName_list = []
            Date_list = []
            ServiceName_list = []
            ServiceResource_list = []
            Quantity_list = []
            Cost_list = []

            df = pd.read_csv("./testfilecsv.csv")
            for i in range(len(df.index)):
                SubscriptionName_list.append(df['SubscriptionName'].values[i])
                Date_list.append(df['Date'].values[i])
                ServiceName_list.append(df['ServiceName'].values[i])
                ServiceResource_list.append(df['ServiceResource'].values[i])
                Quantity_list.append(df['Quantity'].values[i])
                Cost_list.append(df['Cost'].values[i])

        
            All_data = list(set(zip(SubscriptionName_list, Date_list, ServiceName_list,
                                    ServiceResource_list, Quantity_list, Cost_list)))
            # print("alldata",All_data)
            return All_data

        except (Exception, Error) as error:
            print("add_data methode error is:", error)

    def insertIntoTable(self):
        cursor = self.conn.cursor()
        insert = "INSERT INTO resource (SubscriptionName, Date, ServiceName, ServiceResource, Quantity, Cost) VALUES (%s, %s, %s, %s, %s, %s);"
        # print(insert)
        value = self.data_list
        # print(value)
        cursor.executemany(insert, value)
        self.conn.commit()
        cursor.close()


data = Send_Data()
data.insertIntoTable()
print()

