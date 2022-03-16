from machine import Pin, ADC
import wifiConnect
import socket

button = Pin(15, Pin.IN, Pin.PULL_UP)

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

def web_page():
    html_str="""<html>
                 <head> <title>ESP BUTTON EXAMPLE</title>
                 <meta http-equiv="refresh" content="1"> </head>
                 <body> <h1>ESP BUTTON EXAMPLE</h1>
                 <p><h2 style="color:red;"><strong>BUTTON VALUE IS: """ + str(button.value()) + """</strong></h2></p>
                 </body>
                 <style>html{text-align:center}</style>
                 </html>"""
    return html_str
    
def main():
    wifiConnect.connect()
    http_server()
    
if __name__ == "__main__":
    main()