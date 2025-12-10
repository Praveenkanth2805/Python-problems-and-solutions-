import mysql.connector

def db_connect():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="pythonsample"
        )

db_connect()
print("database is initilized")
