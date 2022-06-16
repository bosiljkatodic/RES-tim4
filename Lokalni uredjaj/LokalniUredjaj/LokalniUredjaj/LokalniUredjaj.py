from datetime import datetime
import socket
import time
import Device
import hashlib

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


"""
def konektujNaAMS():
    try:
        AMSSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    print('Cekamo na odgovor konekcije od strane AMS!')
    res = AMSSocket.recv(1024)
    global idTemp
    idTemp = input("Unesite ID uredjaja -> ")
    global stanjeTemp
    stanjeTemp = input("Unesite pocetno stanje -> ")
    temp="{0}/{1}/{2}".format(idTemp,str(datetime.now()),stanjeTemp)
    Send(str.encode(temp), AMSSocket)
"""


def connectingToAMS():  
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client.connect(ADDR)
    return client

def sendAMS(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)
    
def startAMS():
    #answer = input('Would you like to connect (yes/no)? ')
    # if answer.lower() != 'yes':
     #   return

    connection = connectingToAMS()
    #while True:
        #if n == 1: #povezani smo na AMS, sada gledamo da li imamo analogni ili digitali i na osnovu toga pravimo meni
           
    print("Odaberite tip uredjaja:")
    print("DIGITALNI UREDJAJ - 1")
    print("ANALOGNI UREDJAJ - 2")   
    tipUredjaja = int(input(": "))

    if tipUredjaja == 1: #DIGITALNI
        state = "DIGITAL"
        print(state)
        name = input("Unesite ime uredjaja: ") #ime uredjaja
        localDeviceCode = hashlib.md5(name.encode())
        print(localDeviceCode.hexdigest())
        print("Unesite stanje uredjaja: 0 za OFF ili 1 za ON")
        actualValue = int(input(": "))
        timestamp = datetime.timestamp(datetime.now())
        device = "{0}/{1}/{2}/{3}".format(state, localDeviceCode.hexdigest(), actualValue, timestamp)
        #print(device)
        #print(f"Tip uredjaja: {state}, Ime uredjaja: {localDeviceCode}, Stanje: {actualValue}, Vreme: {timestamp}")
            
    elif tipUredjaja == 2: #ANALOGNI
        state = "ANALOG"
        localDeviceCode = input("Unesite ime uredjaja: ") #ime uredjaja
        print("Unesite stanje uredjaja: 0 za OFF ili od 1 do 5")
        actualValue = int(input(": "))
        timestamp = datetime.timestamp(datetime.now())
    else: #pogresan odabir tipa uredjaja
        print("Nepostojeci tip uredjaja. Pokusajte ponovo")   

    sendAMS(connection, device)

    while True:
        print("Odaberite neku od opcija: ")
        print("PROMENA STANJA - 1")
        print("DISCONNECTED - 2")
        opcije = int(input(": "))

        if opcije == 1:
            pass
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
    pass

"""
def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input('Would you like to connect (yes/no)? ')
    if answer.lower() != 'yes':
        return

    connection = connect()
    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')


start()
"""

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
        pass
    else:
         print("Odabrali ste nepostojecu opciju za povezivanje. Pokusajte ponovo.")

    while True:
        if n == 1:
            pass
        elif n == 2: #povezivanje na kontroler
            pass

        else:  #pogresno povezivanje
            pass
           
connecting()
