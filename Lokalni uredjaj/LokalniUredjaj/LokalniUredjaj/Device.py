from datetime import datetime


class Device(object):
    def __init__(self, localDeviceCode, actualValue, state):
        self.localDeviceCode=localDeviceCode 
        self.timestamp = datetime.timestamp(datetime.now())
        self.actualValue = actualValue
        self.state = state #can be analog or digital

#localDeviceCode getter method
def getLocalDeviceCode(self):
    return self.localDeviceCode
#localDeviceCode setter method
def setLocalDeviceCode(self, value):
    self.localDeviceCode = value

#timestamp getter method
def getTimestamp(self):
    return self.timestamp
#timestamp setter method
def setTimestamp(self, value):
    self.timestamp = value

#actualValue getter method
def getActualValue(self):
    return self.actualValue
#actualValue setter method
def setActualValue(self, value):
    self.actualValue = value

#state getter method
def getState(self):
    return self.state
#state setter method
def setState(self, value):
    self.state = value








