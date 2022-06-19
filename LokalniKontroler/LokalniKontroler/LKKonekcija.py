from datetime import datetime
import threading
import socket
import json
import xml.etree.cElementTree as ET
import os
import time
import funkcijeLK
#import database

PORT = 5050
PORT_KONTROLER = 6060
SERVER = "localhost"
ADDR_KONTROLER = (SERVER, PORT_KONTROLER)
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORUKA = ''



clients = set()
clients_lock = threading.Lock()
xml_lock = threading.Lock()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR_KONTROLER)

############
    
###########2  
      
###########3
        
        
#############4

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            #PORUKA = msg
           
            if not msg:
                break

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] {msg}")
                break
            
            def menu():
                while xml_lock.locked():
                    time.sleep(0.001)
                zakljucan = xml_lock.locked()
                #print(zakljucan, "Snimam podatke:", msg)
                xml_lock.acquire()   #zakljucaj
                if not os.path.isfile(fileName) :
                    print('NEMA FAJLA!!!')
                #else :
                #    print('Fajl postoji')
                x = ET.parse(fileName)
                lk = x.getroot()

                ET.SubElement(lk, "data").text = msg

                tree = ET.ElementTree(lk)

                with open (fileName, "wb") as xml_file :
                    tree.write(xml_file)

                #print('Podaci snimljeni', msg)
                xml_lock.release()  #otkljucaj
                
            menu()

            
            print(f"Podaci snimljeni[{addr}] {msg}")

            #with clients_lock:
               # for c in clients:
                 #   c.sendall(f"[{addr}] {msg}".encode(FORMAT))
                    
    except:
        print("OTKAZ OPREME")
        

    finally:
        #conn.close()
        #with clients_lock:
           #clients.remove(conn)
        conn.close()

def start():
    
    print('[SERVER STARTED]!')
    server.listen()
    while True:
        print("Cekam podatke...")
        conn, addr = server.accept()
        handle_client(conn, addr)
        
        with clients_lock:
           clients.add(conn)
           print(clients)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


def azurirajAMS() :
    time.sleep(0.3)
    while xml_lock.locked():
        time.sleep(0.001)
    #dobijen_lock = lock.acquire()
    connection = funkcijeLK.connectingToAMS(ADDR)
    if connection:
        print('AZURIRAM AMS')
        x = ET.parse(fileName)
        lk = x.getroot()
        
            
        if len(lk) > 0 :
            with xml_lock:
            # OVDE posaljemo podatke
                for data in lk:
                    #print('Azuriram:', data.attrib, data.text)
                    funkcijeLK.sendData(connection, data.text)
                    lk.remove(data)
                
                tree = ET.ElementTree(lk)
                
                time.sleep(1)
            
                with open (fileName, "wb") as xml_file:
                    tree.write(xml_file)
                
        print('AZURIRANJE ZAVRSENO')
        connection.close()
        
    #lock.release()
    else:
        print("Ne mogu da se konektujem na AMS trenutno")
        
    
    
def pokreniSlanje():
    poslednjeVremeSlanja = datetime.timestamp(datetime.now())
    while True:
        razlikaVremena = datetime.timestamp(datetime.now()) - poslednjeVremeSlanja
        if razlikaVremena >= float(periodSlanja):
            #posaljiPOdatke
            azurirajAMS()
            #print("Saljem podatke")
            poslednjeVremeSlanja = datetime.timestamp(datetime.now())

name = input("Unesite ime kontrolera: ") #ime kontrolera
fileName = name + ".xml"
postojiKontroler = funkcijeLK.pokreniLK(fileName)
"""

if not postojiKontroler:
    PORT_KONTROLER = int(input("Unesite port kontrolera: ")) #port kontrolera
    dodajKontroler()
else:
    PORT_KONTROLER = ucitajKontroler()
"""    
#ADDR_KONTROLER = (SERVER, PORT_KONTROLER)
#print(ADDR_KONTROLER)


periodSlanja = 5

threading.Thread(target=pokreniSlanje).start()
start()

