from webpage import web_page
import wifiConnect
from machine import Pin
import socket

led = Pin(2, Pin.OUT)

def http_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 80))
    sock.listen(5)
    while True:
      conn, addr = sock.accept()
      print('Got a connection from ', str(addr))
      request = conn.recv(1024)
      request = str(request)
      led_on = request.find('/?led=on')
      led_off = request.find('/?led=off')
      if led_on == 6:
        print('LED ON')
        led.value(1)
      if led_off == 6:
        print('LED OFF')
        led.value(0)
      response = web_page(led.value())
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()
      
def main():
    wifiConnect.connect()
    http_server()
    
if __name__ == "__main__":
    main()