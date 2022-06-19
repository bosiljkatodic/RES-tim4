import csv
from datetime import datetime
import json
import threading
import socket
from database import add_device, connect, create_tables
import os
import xml.etree.cElementTree as ET


PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
DEVICE_EXIST = "exist LocalDeviceCode"
IZVESTAJI = """
Koji izvestaj zelite da napravite?
(Unesite broj od 1 do 5)

1) Listanje svih postojećih uređaja u sistemu
2) Detalji promena za izabrani period za izabrani lokalni uređaj (sve promene + sumarno)
3) Broj radnih sati za izabrani uredjaj za izabrani vremenski period (od, do kalendarski po satima)
4) Izlistavanje svih uredjaja čiji je broj radnih sati preko konfigurisane vrednosti
5) Izadji
Vas izbor:
"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

def menu(msg):
    #print(msg)
    name="data.db"
    connection = connect(name)
    create_tables(connection)
    podaci = msg.split("/")
    razlika = (float(podaci[3]) - vremePokretanjaServera) * ubrzanje   #razlika u sekundama = trenutno vreme - pocetno vreme kada je pokrenut server
    novoVreme = vremePokretanjaServera + razlika 
    date = datetime.fromtimestamp(novoVreme).strftime('%Y-%m-%d %H:%M:%S')

    return add_device(connection, podaci[0], podaci[1], podaci[2], date)

def print_all_devices():
    name="data.db"

    connection = connect(name)

    c = connection.cursor()
    
    sqlStatement = "SELECT * FROM devices;"
    c.execute(sqlStatement)
    result = c.fetchall()
    
    with open("new_file.csv", "w") as file:
        csv.writer(file).writerow(x[0] for x in c.description)

        for row in result:
            csv.writer(file).writerow(row)
    c.close()
    del c                

def print_changes_for_device():
    name="data.db"

    connection = connect(name)

    c = connection.cursor()
    localDeviceCode = input("Unesite localDeviceCode za zeljeni uredjaj:")
    timestampStart = input("Unesite pocetak vremenskog intervala, npr. 2022-06-18 13:49:01 :")
    timestampStop = input("Unesite kraj vremenskog intervala, npr. 2022-06-18 13:49:01 :")

    sqlStatement = "SELECT * FROM devices WHERE localDeviceCode = ? AND timestamp >= ? AND timestamp <= ?;"
    c.execute(sqlStatement,(localDeviceCode,timestampStart, timestampStop, ))
    result = c.fetchall()
    
    with open("izvjestaj_1_file.csv", "w") as file:
        csv.writer(file).writerow(x[0] for x in c.description)

        for row in result:
            csv.writer(file).writerow(row)
    print("Ukupan broj promjena stanja:")
    print(len(result))
    c.close()
    del c 
"""
def get_work_hours_for_period_and_localdevicecode():
    with open('izvjestaj_1_file.csv', newline='') as csvfile:
        devicereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for list in devicereader:
            for row in list:
            #podaci1 = row.split(",")
            #actualValue = podaci1[3]
            #print(actualValue)
                print("Red",row)
                s1 = row.split(",")[0]
                
                #s2 = s1.split(",")[3]
                #print("Actual value ",s2)
                print(s1)
                oddrow = row[1::2]
                evenrow = row[2::2]
                print(Parni:oddrow)
       # for o in oddrow:
        #    for e in evenrow:
         #       spojen =  o+e
          #      print(spojen)

    """            
        
def izvestaji():
    #print_all_devices()

    while(user_input := input(IZVESTAJI)) != "5":
        if user_input == "1":
            print_all_devices()
        elif user_input == "2":
            print_changes_for_device()
        elif user_input == "3":
           # get_work_hours_for_period_and_localdevicecode()
           
           pass
        else:
            print("Uneli ste nepostojecu opciju. Pokusajte ponovo.")
                
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)

            if not msg:
                break

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] {msg}")
                break

            if msg == DEVICE_EXIST:
                pass

            #upisivanje u bazu
            
                
            menu(msg)

            print(f"[{addr}] {msg}")
            
           # with clients_lock:
                #for c in clients:
                    #c.sendall(f"[{addr}] {msg}".encode(FORMAT))
                    
    except ConnectionResetError:
        print("OTKAZ OPREME")
        
    finally:
        #with clients_lock:
            #clients.remove(conn)

        conn.close()
        izvestaji()
        
def Ubrzanje():
    localDeviceConfig = "Vreme.xml"
    #print(localDeviceConfig)
    
    if not os.path.isfile(localDeviceConfig): #ako je xml prazan
        return 1 #jedna realna sek  = jedna sek u sistemu
    else:
        x = ET.parse(localDeviceConfig)
        lu = x.getroot()
            
         
        for data in lu:
            if data.tag == "ubrzanje":
                return int(data.text)
            
        
    

ubrzanje = Ubrzanje()
#quit()
print('[SERVER STARTED]!')
vremePokretanjaServera = datetime.timestamp(datetime.now())
date = datetime.fromtimestamp(vremePokretanjaServera).strftime('%Y-%m-%d %H:%M:%S') #prebacivanje vremePOkretanjaSErvera u lepsi ispis
print("Vreme pokretanje servera: ", date)

server.listen()
while True:
    conn, addr = server.accept()
    with clients_lock:
        clients.add(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()



