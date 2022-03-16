from utime import sleep
import network
import socket

myMesg = "HELLO THIS IS A TEST"

def wifiConnect():
    ssid = "yourSSID"
    password = "yourPASSWORD"
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    print("connecting to network")
    while station.isconnected() == False:
        print('.', end='')
        sleep(.1)
    print("\n ---- Connection successful ----")
    print(station.ifconfig())
    ipData = station.ifconfig()
    print("my IP address is: ", ipData[0])

def web_page():
    html_str="""<html>
                <body> <h1>""" + myMesg + """</h1>
                </body>
                </html>"""
    return html_str

def http_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 80))
    sock.listen(5)
    while True:
      client, addr = sock.accept()
      print('Client %s is connected' % str(addr))
      request = client.recv(1024)
      request = str(request)
      response = web_page()
      client.send('HTTP/1.1 200 OK\n')
      client.send('Content-Type: text/html\n')
      client.send('Connection: close\n\n')
      client.sendall(response)
      client.close()
    
wifiConnect()
http_server()