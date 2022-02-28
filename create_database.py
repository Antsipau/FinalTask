import psycopg2
from psycopg2 import Error


def create_connection_to_database():
    try:
        connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
        mycursor = connection.cursor()
        mycursor.execute("INSERT INTO auth_group(name) VALUES('TestGroup')")
        connection.commit()
        mycursor.close()
        connection.close()
        print("Successful connection to database")
    except Error as e:
        print(f"Connection error {e} occurred")

    return connection


print(create_connection_to_database())