from multiprocessing import connection
import sqlite3

CREATE_DEVICES_TABLE = "CREATE TABLE IF NOT EXISTS devices (localDeviceCode TEXT PRIMARY KEY, timestamp TIMESTAMP, actualValue INTEGER, state TEXT);"
INSERT_DEVICE = "INSERT INTO devices (localDeviceCode, timestamp, actualValue, state) VALUES (?, ?, ?, ?);"
GET_ALL_DEVICES = "SELECT * FROM devices;"

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection: 
        connection.execute(CREATE_DEVICES_TABLE)

def add_device(connection, localDeviceCode, timestamp, actualValue, state):
    with connection:
        connection.execute(INSERT_DEVICE, (localDeviceCode, timestamp, actualValue, state))

def get_all_devices(connection):
    with connection:
        return connection.execute(GET_ALL_DEVICES).fetchall()


