from digi.xbee.devices import XBeeDevice
device = XBeeDevice("COM1", 9600)
device.open()
device.send_data_broadcast("Hello XBee World!")
device.close()