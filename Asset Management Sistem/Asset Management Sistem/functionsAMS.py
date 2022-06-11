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
            timestamp = input("Enter date: ")
            actualValue = input("Enter actual value(ON, OFF, OPEN or CLOSE): ")
            state = input("Enter state(DIGITAL or ANALOG): ")
            database.add_device(connection, localDeviceCode, timestamp, actualValue, state)
        elif user_input == "2":
            devices = database.get_all_devices(connection)

            for device in devices:
                print(device)

        

        else:
            print("Invalid input, please try again!")
        


menu()
