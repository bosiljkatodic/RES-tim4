from distutils.command.config import config
import os
from pickle import FALSE
from unicodedata import name 
import xml.etree.cElementTree as ET


def ucitajKonfiguracijuLokalnogUredjaja(name):
    localDeviceConfig = name + ".xml"
    #print(localDeviceConfig)
    
    if not os.path.isfile(localDeviceConfig):
        return False  
    else:
        x = ET.parse(localDeviceConfig)
        lu = x.getroot()
        
        #return '{"tipUredjaja":"1","localDeviceCode":"2547886977685f63f06a4d1c10f71a9f","konekcijaNA":"1","periodSlanja":"50"}'
    
        config = "{" 
        for data in lu:
            config += '"' + data.tag + '":"' + data.text + '",' #"state": state,
        config = config[:-1]
        config += "}"
        
        
        return config
            
    """
    device = {
              "state": state, 
              "localDeviceCode": localDeviceCode.hexdigest(),   
              "periodSlanjaPodataka": period
             }
    """
def napraviKonfiguracijuLokalnogUredjaja(name, tipUredjaja, localDeviceCode, konekcijaNA, periodSlanja):
    localDeviceConfig = name + ".xml"
    lu = ET.Element("lokalniUredjaj")
    ET.SubElement(lu, "tipUredjaja").text = str(tipUredjaja)  
    ET.SubElement(lu, "localDeviceCode").text = localDeviceCode  
    ET.SubElement(lu, "konekcijaNA").text = str(konekcijaNA)  
    ET.SubElement(lu, "periodSlanja").text = str(periodSlanja)  

    tree = ET.ElementTree(lu)
      
    with open (localDeviceConfig, "wb") as xml_file :
        tree.write(xml_file)
        
    print('XML FAJL KREIRAN')
    if(tree!=None):
        return "Fajl kreiran"


  