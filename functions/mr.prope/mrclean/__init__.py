import logging
import psycopg2
from psycopg2 import Error
import azure.functions as func
import pandas as pd
import io 
import csv

def connect():
    # Construct connection string
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="adminadmin@spiderpostgres", password="oMCJkAmCdfE.awyJ!oJ9UmQq",
                                      host="spiderpostgres.postgres.database.azure.com",
                                      port="5432", database="monitoring", sslmode="require")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("Connected to the database")
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


def select(table):
    conn = connect()
    cursor = conn.cursor()
    # Fetch all rows from table
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    # Print all rows
    cursor.close()
    conn.close()
    return rows

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n" f"Name: {myblob.name}\n" f"Blob Size: {myblob.length} bytes")

    data = myblob.read()
    #with open("jojo.csv", mode="w") as output:
    #   output.write(str(data))

    with open('jojo.csv', 'w', encoding='iso-8859-1', newline='\n') as csvfile:
        a = b'\x8b'
        b = a.decode("iso-8859-1")
        w = csv.writer(data)
        w.writerow([b])
            
    with open('jojo.csv', 'r', newline='\n', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

        
    #print(pd.read_csv(myblob.read()))

    #my_file = io.StringIO(request.FILES[myblob].read())

    #df = pd.read_csv(myblob)
    #print(df)
    # connect()
    # result = select("resource")
    # print(result)
    # logging.info(result)
