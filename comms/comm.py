from digi.xbee.devices import XBeeDevice

class communicator(object):
    
    def __init__(self):
        self.device = XBeeDevice("COM1", 9600)
        self.device.open()
        self.device.send_data_broadcast("Time to start")

    def sendMessage(self, message):
        self.device.send_data_broadcast(message)
    
    def stop(self):
        self.device.close()