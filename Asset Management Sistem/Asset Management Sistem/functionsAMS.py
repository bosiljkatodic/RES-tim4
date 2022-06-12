import datetime
import database

MENU_PROMPT = """
CHOOSE OPTION:

1) ADD 
2) SEE ALL
3) EXIT
4) GET CHANGES 
Your selection: 
"""

def menu():

    connection = database.connect()
    database.create_tables(connection)

    while(user_input := input(MENU_PROMPT)) != "3":
        if user_input == "1":
            localDeviceCode = input("Enter local Device Code: ")
            timestamp = input("Enter date, example 2022-05-22 09:26:03: ")
            actualValue = input("Enter actual value(ON, OFF, OPEN or CLOSE): ")
            state = input("Enter state(DIGITAL or ANALOG): ")

            database.add_device(connection, localDeviceCode, timestamp, actualValue, state)

        elif user_input == "2":
            devices = database.get_all_devices(connection)
            print("Spisak svih lokalnih uređaja: ")

            for device in devices:
                print(device)

        elif user_input == "4":
            #ispis svih uredjaja
            devices = database.get_all_devices(connection)
            print("Spisak svih lokalnih uređaja: ")
            for device in devices:
                print(device)

            localDeviceCode1 = input("Enter local Device Code: ")
            timestampStart = input("Enter start of period (example 2022-05-22 09:26:03): ")
            timestampStop = input("Enter end of period (example 2022-05-22 09:26:03): ")            
            changes = database.get_changes_by_localDeviceCode(connection, localDeviceCode1, timestampStart, timestampStop)
            print("Sve promjene za izabrani lokalni uredjaj su: ")
            
            for device in changes:
                print("Actual value:")
                print({device[2]})
        else:
            print("Invalid input, please try again!")
        

def accept_message(server):
    clientSocket, address=server.accept()
    print(f"Connesciton from {address} has been established!")

