from importlib import import_module
import unittest
from funkcijeLK import connectingToAMS
from funkcijeLK import sendData
from funkcijeLK import napraviXML
from funkcijeLK import pokreniLK
def test_connectingToAMS():
    
    assert connectingToAMS(("localhost",5050))==False


def test_sendData():
    assert sendData(client=None,data="poruka")=="Nema klijenta"
    assert sendData(client=12,data="")=="Nema poruke"
    
def test_pokreniLK():
    assert pokreniLK("Vreme")==True
    assert pokreniLK("n116wb")==False 
    
def test_napraviXML():
    assert napraviXML("")=="Prazno ime"  
    assert napraviXML("probaXML")==True  
    
       