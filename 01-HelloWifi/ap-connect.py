'''
This is a minimal code to establish an access point using an ESP32.
Run the code and then, using a computer or a smartphone,
verify that the device appears available as a wireless network.
'''
from utime import sleep
import network

#change network name and password to your choosing
ssid = 'MCU'
password = '12345'

#create an instance of network object
ap = network.WLAN(network.AP_IF)

#activate the network
ap.active(True)
#configure characteristics of the network
ap.config(essid=ssid, password=password)

#wait until network is established
while ap.active() == False:
    print('.', end='')
    sleep(.1)

#print out IP information
print("\n ---- Connection successful ----")
print(ap.ifconfig())
ipData = ap.ifconfig()
print("my IP address is: ", ipData[0])

