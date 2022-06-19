import unittest
from funkcijeLokalniUredjaj import connectingToAMS
from funkcijeLokalniUredjaj import connectingToLK

def test_connectingToAMS():
    assert connectingToAMS()==False
    
def test_connectingToLK():
    assert connectingToLK()==False
    


