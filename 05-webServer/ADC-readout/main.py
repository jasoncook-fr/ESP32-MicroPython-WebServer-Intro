from microWebSrv import MicroWebSrv
from machine import Pin, ADC
from utime import sleep

# preparations for ADC input
sensor = ADC(Pin(35))            
sensor.atten(ADC.ATTN_11DB)       #Full range: 3.3v
sensor.width(ADC.WIDTH_12BIT)     #set 12 bit return values (0-4095)

def _httpHandlerDHTGet(httpClient, httpResponse):
    try:
        data = sensor.read()
        print("")
        
    except:
        data = 'Attempting to read sensor...'
        
    httpResponse.WriteResponseOk(
        headers = ({'Cache-Control': 'no-cache'}),
        contentType = 'text/event-stream',
        contentCharset = 'UTF-8',
        content = 'data: {0}\n\n'.format(data) )

routeHandlers = [ ( "/dht", "GET",  _httpHandlerDHTGet ) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)