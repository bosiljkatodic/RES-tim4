from datetime import datetime
import socket
import time
import hashlib
import json

#pokusaj pushovanja na git obrisati posle ovaj komentar
PORT = 5050
PORT_KONTROLER = 6060
SERVER = "localhost"
ADDR = (SERVER, PORT)
ADDR_KONTROLER = (SERVER, PORT_KONTROLER)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

def connectingToAMS():  
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client.connect(ADDR)
    return client

def sendAMS(client, msg):    
    message = msg.encode(FORMAT)
    client.send(message)
    
def startAMS():
    
    connection = connectingToAMS()
       
    print("Odaberite tip uredjaja:")
    print("DIGITALNI UREDJAJ - 1")
    print("ANALOGNI UREDJAJ - 2")   
    tipUredjaja = int(input(": "))

    if tipUredjaja == 1: #DIGITALNI
        state = "DIGITAL"
        #print(state)
        name = input("Unesite ime uredjaja: ") #ime uredjaja
        localDeviceCode = hashlib.md5(name.encode())
        #print(localDeviceCode.hexdigest())
        print("Unesite stanje uredjaja: 0 za OFF ili 1 za ON")
        actualValue = int(input(": "))
        timestamp = datetime.timestamp(datetime.now())
        device = "{0}/{1}/{2}/{3}".format(state, localDeviceCode.hexdigest(), actualValue, timestamp)
        
        #print(f"Tip uredjaja: {state}, Ime uredjaja: {localDeviceCode}, Stanje: {actualValue}, Vreme: {timestamp}")

            
    elif tipUredjaja == 2: #ANALOGNI
        state = "ANALOG"
        name = input("Unesite ime uredjaja: ") #ime uredjaja
        localDeviceCode = hashlib.md5(name.encode())
        print("Unesite stanje uredjaja: 0 za OFF ili od 1 do 5")
        actualValue = int(input(": "))
        timestamp = datetime.timestamp(datetime.now())
        device = "{0}/{1}/{2}/{3}".format(state, localDeviceCode.hexdigest(), actualValue, timestamp)

    else: #pogresan odabir tipa uredjaja
        print("Nepostojeci tip uredjaja. Pokusajte ponovo")   

    sendAMS(connection, device)

    while True:
        print("Odaberite neku od opcija: ")
        print("PROMENA STANJA - 1")
        print("DISCONNECTED - 2")
        opcije = int(input(": "))

        if opcije == 1:
            if tipUredjaja == 1: #digitalni
                print("Unesite novo stanje uredjaja: 0 za OFF ili 1 za ON")
            elif tipUredjaja == 2: #analogni
                print("Unesite novo stanje uredjaja: 0 za OFF ili od 1 do 5")
                
            actualValue = int(input(": "))  #novo stanje
            stanje = device.split('/') #splitovanje device stringa
            stanje[2] = actualValue
            device = "{0}/{1}/{2}/{3}".format(state, localDeviceCode.hexdigest(), stanje[2], timestamp)

            sendAMS(connection, device)

        elif opcije == 2:
            sendAMS(connection, DISCONNECT_MESSAGE)
            time.sleep(1)
            print('Disconnected')
            break
        else:
            print("niste izabrali odgovarajucu opciju. Pokusajte ponovo.")

    #sendAMS(connection, DISCONNECT_MESSAGE)
    #time.sleep(1)
    #print('Disconnected')


def connectingToLK():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client.connect(ADDR_KONTROLER)
    return client

def sendLK(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def startLK():

    connection = connectingToLK()
           
    print("Odaberite tip uredjaja:")
    print("DIGITALNI UREDJAJ - 1")
    print("ANALOGNI UREDJAJ - 2")   
    tipUredjaja = int(input(": "))

    if tipUredjaja == 1: #DIGITALNI
        state = "DIGITAL"
        #print(state)
        name = input("Unesite ime uredjaja: ") #ime uredjaja
        localDeviceCode = hashlib.md5(name.encode())
        #print(localDeviceCode.hexdigest())
        print("Unesite stanje uredjaja: 0 za OFF ili 1 za ON")
        actualValue = int(input(": "))
        timestamp = datetime.timestamp(datetime.now())
        #device = "{0}/{1}/{2}/{3}".format(state, localDeviceCode.hexdigest(), actualValue, timestamp)

        device = {"state": state, 
                  "localDeviceCode": localDeviceCode.hexdigest(), 
                  "actualValue": actualValue, 
                  "timestamp": timestamp
                 } 

        y = json.dumps(device)
        print(y)

    elif tipUredjaja == 2: #ANALOGNI
        state = "ANALOG"
        name = input("Unesite ime uredjaja: ") #ime uredjaja
        localDeviceCode = hashlib.md5(name.encode())
        print("Unesite stanje uredjaja: 0 za OFF ili od 1 do 5")
        actualValue = int(input(": "))
        timestamp = datetime.timestamp(datetime.now())
        device = "{0}/{1}/{2}/{3}".format(state, localDeviceCode.hexdigest(), actualValue, timestamp)
        
    else: #pogresan odabir tipa uredjaja
        print("Nepostojeci tip uredjaja. Pokusajte ponovo")   

    sendLK(connection, y)

    while True:
        print("Odaberite neku od opcija: ")
        print("PROMENA STANJA - 1")
        print("DISCONNECTED - 2")
        opcije = int(input(": "))

        if opcije == 1:
            if tipUredjaja == 1: #digitalni
                print("Unesite novo stanje uredjaja: 0 za OFF ili 1 za ON")
            elif tipUredjaja == 2: #analogni
                print("Unesite novo stanje uredjaja: 0 za OFF ili od 1 do 5")
                
            actualValue = int(input(": "))  #novo stanje
            stanje = device.split('/') #splitovanje device stringa
            stanje[2] = actualValue
            device = "{0}/{1}/{2}/{3}".format(state, localDeviceCode.hexdigest(), stanje[2], timestamp)

            sendLK(connection, device)

        elif opcije == 2:
            sendLK(connection, DISCONNECT_MESSAGE)
            time.sleep(1)
            print('Disconnected')
            break
        else:
            print("niste izabrali odgovarajucu opciju. Pokusajte ponovo.")


#startAMS()

#f-ja za izbor povezivanja
def connecting():
    print("Odaberite na sta zelite da se povezete: ")
    print("AMS - unesite broj 1")
    print("Lokalni kontroler - unesite broj 2")
    n = int(input("Povezujem se na: "))  #promenljiva za konekciju

    if n == 1 :
        print("Povezan sam na AMS")
        startAMS()

    elif n == 2:
        print("Povezan sam na lokalni kontroler")
        startLK()
    else:
         print("Odabrali ste nepostojecu opciju za povezivanje. Pokusajte ponovo.")

    
connecting()
