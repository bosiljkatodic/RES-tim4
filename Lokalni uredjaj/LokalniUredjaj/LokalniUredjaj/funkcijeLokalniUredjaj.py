from datetime import datetime
from distutils.command.config import config
import os
import socket
import time
import hashlib
import json
import XMLProvere #import ucitajKonfiguracijuLokalnogUredjaja as ucitajKLU
import random
import xml.etree.cElementTree as ET

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