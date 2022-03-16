'''
This is a minimal code to establish an access point using an ESP32.
Run the code and then, using a computer or a smartphone,
verify that the device appears available as a wireless network.
'''
from utime import sleep
import network
import gc
# common practice to use garbage collect
gc.collect()

#sleep 2 seconds at startup in case we need to intervene for reprogramming
sleep(2)

# change network name and password to your choosing
ssid = 'MCU'
password = '12345'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

