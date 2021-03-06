from datetime import datetime
import threading
import socket
import json
import xml.etree.cElementTree as ET
import os
import time

FORMAT = "utf-8"

def connectingToAMS(inputADDR): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    try:
        client.connect(inputADDR)
        return client
    except ConnectionRefusedError:
        print("AMS je nedostupan")
        return False
    
def sendData(client, data):
    #podaci = json.loads(data)
    #date = datetime.fromtimestamp(float(podaci["timestamp"])).strftime('%Y-%m-%d %H:%M:%S')
        #database.add_device(connection, podaci["state"], podaci["localDeviceCode"], podaci["actualValue"], date)
    
    #device = "{0}/{1}/{2}/{3}".format(state, localDeviceCode.hexdigest(), actualValue, timestamp)
    #message = "{0}/{1}/{2}/{3}".format(podaci["state"], podaci["localDeviceCode"], podaci["actualValue"], podaci["timestamp"])  
    """
    message = {"state": podaci["state"], 
               "localDeviceCode": podaci["localDeviceCode"], 
                "actualValue": podaci["actualValue"], 
                "timestamp": podaci["timestamp"]
                }
    """
    ##y = json.dumps(message)
    if(client==None):
        return "Nema klijenta"
    elif(data==""):
        return "Nema poruke"
    message = data.encode(FORMAT)
    client.send(message)   
    
def napraviXML(inputFileName):
    if(inputFileName=="" or inputFileName==None):
        return "Prazno ime"
    lk = ET.Element("lokalniKontroler")
    tree = ET.ElementTree(lk)
      
    with open (inputFileName, "wb") as xml_file :
        tree.write(xml_file)
        
    print('XML FAJL KREIRAN')
    if(tree!=None):
        return True
    
def pokreniLK(inputFileName) :
    #print("Pokrecem LK")
    # proveravamo da li postoji XML fajl
    if not os.path.isfile(inputFileName):
        napraviXML(inputFileName)
        return False
    else:
        print('Fajl postoji')
        return True   

#def dodajKontroler():
#   fileNameKontroleri = r"C:\Users\Korisnik\Desktop\res\Clone - 18.6\RES-tim4\Kontroleri.xml"
#    if not os.path.isfile(fileNameKontroleri) :
#        print('NEMA FAJLA!!!')
#    #else :
#    #    print('Fajl postoji')
#    x = ET.parse(fileNameKontroleri)
#    lk = x.getroot()

#    k = ET.SubElement(lk, 'Kontroler')
#    ET.SubElement(k, 'Naziv').text = name
#    ET.SubElement(k, 'Port').text = str(PORT_KONTROLER)

#    tree = ET.ElementTree(lk)

#    with open (fileNameKontroleri, "wb") as xml_file :
#        tree.write(xml_file)
 
#def ucitajKontroler():
#    fileNameKontroleri = r"C:\Users\Korisnik\Desktop\res\Clone - 18.6\RES-tim4\Kontroleri.xml"
#    #print(localDeviceConfig)
    
#    if not os.path.isfile(fileNameKontroleri):
#        return 1 #jedna realna sek  = jedna sek u sistemu
#    else:
#        x = ET.parse(fileNameKontroleri)
#        lk = x.getroot()

        
#        for k in lk.findall('Kontroler'):
#            if k.find('Naziv').text == name:
#                port = k.find('Port').text
#                return int(port)      
                