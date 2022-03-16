import network
from utime import sleep

#wlan name and password
ssid = "stumo"
password = "thinkdifferent"

#create instance of network object
station = network.WLAN(network.STA_IF)

#activate network interface
station.active(True)

#connect to the wifi network
station.connect(ssid, password)
print("connecting to network")

#wait until network is established
while station.isconnected() == False:
    print('.', end='')
    sleep(.1)

#print out IP information
print("\n ---- Connection successful ----")
print(station.ifconfig())
ipData = station.ifconfig()
print("my IP address is: ", ipData[0])

