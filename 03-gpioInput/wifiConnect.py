import network
from utime import sleep

ssid = "yourSSID"
password = "yourPassword"
station = network.WLAN(network.STA_IF)

def connect():
    station.active(True)
    station.connect(ssid, password)
    print("connecting to network")
    while station.isconnected() == False:
        print('.', end='')
        sleep(.1)
    print("\n ---- Connection successful ----")
    ipData = station.ifconfig()
    print("my IP address is: ", ipData[0])
