from multiprocessing import connection
import sqlite3

CREATE_DEVICES_TABLE = "CREATE TABLE IF NOT EXISTS devices (state TEXT, localDeviceCode TEXT PRIMARY KEY, actualValue INTEGER, timestamp DATETIME);"
INSERT_DEVICE = "INSERT INTO devices (state, localDeviceCode, actualValue, timestamp) VALUES (?, ?, ?, ?);"
GET_ALL_DEVICES = "SELECT * FROM devices;"
GET_CHANGES_BY_LOCAL_DEVICE_CODE_AND_PERIOD = "SELECT * FROM devices WHERE localDeviceCode = ? AND timestamp >= ? AND timestamp <= ?;"

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection: 
        connection.execute(CREATE_DEVICES_TABLE)

def add_device(connection, state, localDeviceCode, actualValue, timestamp):
    with connection:
        connection.execute(INSERT_DEVICE, (state, localDeviceCode, actualValue, timestamp))

def get_all_devices(connection):
    with connection:
        return connection.execute(GET_ALL_DEVICES).fetchall()

def get_changes_by_localDeviceCode(connection, localDeviceCode, timestampStart, timestampStop):
    with connection:
        return connection.execute(GET_CHANGES_BY_LOCAL_DEVICE_CODE_AND_PERIOD, (localDeviceCode,timestampStart, timestampStop, )).fetchall()
