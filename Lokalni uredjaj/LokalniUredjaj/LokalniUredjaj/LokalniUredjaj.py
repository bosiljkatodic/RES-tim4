from datetime import datetime
from distutils.command.config import config
import socket
import time
import hashlib
import json
import XMLProvere #import ucitajKonfiguracijuLokalnogUredjaja as ucitajKLU
import random

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
    try:
        client.connect(ADDR)
        return client
    except ConnectionRefusedError:
        print("AMS je nedostupan")
        return False
    
def connectingToLK():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    try:
        client.connect(ADDR_KONTROLER)
        return client
    except ConnectionRefusedError:
        print("Kontroler je nedostupan")
        return False
   
def sendData(client):
   # print(tipUredjaja, type(tipUredjaja))
    
    if int(tipUredjaja) == 1:
        actualValue = random.randint(0, 1)
    else:
        actualValue = random.randint(0, 100)
    #podaci = json.loads(data)
    message = "{0}/{1}/{2}/{3}".format(tipUredjaja, hashlib.md5(name.encode()).hexdigest(), actualValue, datetime.timestamp(datetime.now()))  
   
    print(message)   
    """
    message = {"state": tipUredjaja, 
               "localDeviceCode": hashlib.md5(name.encode()).hexdigest(), 
                "actualValue": actualValue, 
                "timestamp": datetime.timestamp(datetime.now())
                }
    
    y = json.dumps(message)
    """
    message = message.encode(FORMAT)
    client.send(message)




#f-ja za izbor povezivanja
def connecting(tipKonekcije):
    
    if tipKonekcije == 1:
        print("Povezujem se sa AMS-om ...")
        connection = connectingToAMS()
        return connection
    
    elif tipKonekcije == 2:
        print("Povezujem se na lokalni kontroler...")
        connection = connectingToLK()
        return connection
       

def TipUredjaja():
    print("Odaberite tip uredjaja:")
    print("DIGITALNI UREDJAJ - 1")
    print("ANALOGNI UREDJAJ - 2")   
    tipUredjaja = input(": ")
    
     
    if tipUredjaja == "1" or tipUredjaja == "2":
        return int(tipUredjaja)
    else:
        print("Izabrali ste nepostojecu opciju. Pokusajte ponovo.")
        TipUredjaja() 

def TipPovezivanja():
    print("Odaberite na sta zelite da se povezete: ")
    print("AMS - unesite broj 1")
    print("Lokalni kontroler - unesite broj 2")
    konekcijaNA = input("Povezujem se na: ")  #promenljiva za konekciju  
    
    if konekcijaNA == "1" or konekcijaNA == "2":
        return int(konekcijaNA)
    else:
        print("Izabrali ste nepostojecu opciju. Pokusajte ponovo.")
        TipPovezivanja() 
    
def PeriodSlanja():
    print("Izaberi period slanja podataka u sekundama: ")
    periodSlanja = input("Period slanja podataka: ")
    
    if periodSlanja.strip().isdigit(): #da bi se iput pretcvorio u int 
        return int(periodSlanja)
    else:
        print("Izabrali ste nepostojecu opciju. Pokusajte ponovo.")
        PeriodSlanja()

#MAIN      
name = input("Unesite ime uredjaja: ") #ime uredjaja
localDeviceCode = hashlib.md5(name.encode()).hexdigest()

config = XMLProvere.ucitajKonfiguracijuLokalnogUredjaja(str(name))

if config: #postoji vec taj uredjaj
    #print("Postoji konf fajl", config)
    config = json.loads(config)

    tipUredjaja = int(config["tipUredjaja"])
    konekcijaNA = int(config["konekcijaNA"])
    periodSlanja = int(config["periodSlanja"])
    print(tipUredjaja, konekcijaNA, periodSlanja)
    #print(config)
    

    
else: #posto ne postoji cong fajl, znaci da imamo novi uredjaj
    print("Ne postoji konf fajl")
    
    tipUredjaja = TipUredjaja()
    konekcijaNA = TipPovezivanja()
    periodSlanja = PeriodSlanja()
    XMLProvere.napraviKonfiguracijuLokalnogUredjaja(name, tipUredjaja, localDeviceCode, konekcijaNA, periodSlanja)   

#posalji prve podatke
connection = connecting(int(konekcijaNA))
if not connection:
    quit()
    
sendData(connection)

poslednjeVremeSlanja = datetime.timestamp(datetime.now())

while True:  # slanje podataka na svaki intervalu PeriodSLanja npr svakih 5 sek
    razlikaVremena = datetime.timestamp(datetime.now()) - poslednjeVremeSlanja
    
    if razlikaVremena >= float(periodSlanja):
        #posaljiPOdatke
        sendData(connection)
        #print("Saljem podatke")
        #time.sleep(0.5)

        poslednjeVremeSlanja = datetime.timestamp(datetime.now())

