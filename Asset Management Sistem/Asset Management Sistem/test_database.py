import pytest
import database
from datetime import datetime
import unittest
import sqlite3
import hashlib
from unittest import mock

def test_connect():
    assert database.connect("data.db") != None
    assert database.connect("") == "Prazno"
    assert database.connect("alen.jk") == "Los format"

def test_create_tables():
    
    assert database.create_tables(connection=sqlite3.connect("proba.db"))!=None
    assert database.create_tables(None)=="Nema konekcije"
      
def test_add_device():
    
    assert database.add_device(connection=sqlite3.connect("proba.db"),state="1",
                               localDeviceCode="jhbbyuvhvbwdns",actualValue=1,
                               timestamp=datetime.timestamp(datetime.now()))!=None
    assert database.add_device(connection=None,state="1",localDeviceCode="aaaa",actualValue=1,
                               timestamp=datetime.timestamp(datetime.now()))=="Nema konekcije"
    assert database.add_device(connection=sqlite3.connect("proba.db"),state="abdc",localDeviceCode="bhvvcjhbbbwdns",actualValue=1,
                               timestamp=datetime.timestamp(datetime.now()))=="Loš state"
    assert database.add_device(connection=sqlite3.connect("proba.db"),state="1",localDeviceCode="",actualValue=1,
                               timestamp=datetime.timestamp(datetime.now()))=="Loš localDeviceKod"
    assert database.add_device(connection=sqlite3.connect("proba.db"),state="1",localDeviceCode="vsv",actualValue=None,
                               timestamp=datetime.timestamp(datetime.now()))=="Loš actualValue"
    assert database.add_device(connection=sqlite3.connect("proba.db"),state="1",localDeviceCode="vuv",actualValue=1,
                               timestamp=None)=="Loš timestamp" 
  
def test_get_all_devices():
    assert database.get_all_devices(connection=sqlite3.connect("proba.db"))!=None   
    assert database.get_all_devices(connection=None)=="Nema konekcije"  
    
def test_get_changes_by_localDeviceCode():
    assert database.get_changes_by_localDeviceCode(connection=sqlite3.connect("proba.db"),localDeviceCode="fbnjvnsk",
                                                   timestampStart=datetime.timestamp(datetime.now()),timestampStop=datetime.timestamp(datetime.now()))!=None
    assert database.get_changes_by_localDeviceCode(connection=None,localDeviceCode="fbnjvnsk",
                                                   timestampStart=datetime.timestamp(datetime.now()),
                                                   timestampStop=datetime.timestamp(datetime.now()))=="Nema konekcije"
    assert database.get_changes_by_localDeviceCode(connection=sqlite3.connect("proba.db"),localDeviceCode=None,
                                                   timestampStart=datetime.timestamp(datetime.now()),
                                                   timestampStop=datetime.timestamp(datetime.now()))=="Loš localDeviceKod"
    assert database.get_changes_by_localDeviceCode(connection=sqlite3.connect("proba.db"),localDeviceCode="jhcbwhkvnj",
                                                   timestampStart=None,
                                                   timestampStop=datetime.timestamp(datetime.now()))=="Loš timestamp"
    assert database.get_changes_by_localDeviceCode(connection=sqlite3.connect("proba.db"),localDeviceCode="jhcbwhkvnj",
                                                   timestampStart=datetime.timestamp(datetime.now()),
                                                   timestampStop=None)=="Loš timestamp"
    
    
    
    
    
        