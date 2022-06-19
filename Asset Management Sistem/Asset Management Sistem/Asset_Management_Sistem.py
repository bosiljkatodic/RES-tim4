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

    add_device(connection, podaci[0], podaci[1], podaci[2], date)
                
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



