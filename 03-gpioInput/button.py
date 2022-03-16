#button code provided for simple test purposes
from machine import Pin
from utime import sleep
   
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    buttonState = button.value()
    print(buttonState)
    sleep(.2)
