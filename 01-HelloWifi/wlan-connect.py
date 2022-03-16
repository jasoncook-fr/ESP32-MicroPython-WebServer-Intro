import network
from utime import sleep

ssid = "stumo"
password = "thinkdifferent"

#connect to local wireless network
station = network.WLAN(network.STA_IF)

#activate network interface
station.active(True)

# Connect to the wifi network
station.connect(ssid, password)
print("connecting to network")

while station.isconnected() == False:
    print('.', end='')
    sleep(.1)

print("\n ---- Connection successful ----")
print(station.ifconfig())

ipData = station.ifconfig()
print("my IP address is: ", ipData[0])

