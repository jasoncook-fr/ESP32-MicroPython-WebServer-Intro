from machine import Pin, ADC
from utime import sleep

# preparations for ADC input
pot = ADC(Pin(35))             #on most boards, pin 36 is ADC0 
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
pot.width(ADC.WIDTH_12BIT)     #set 12 bit return values (0-4095)

while True:
    # read the potentiometer and print its' value
    pot_value = pot.read()
    print("potVal : ", pot_value)   
    # tiny delay
    sleep(.01)

