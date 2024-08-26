from machine import Pin
from time import sleep

button = Pin(15, Pin.IN)
button2 = Pin(14, Pin.IN)
led1 = Pin(28, Pin.OUT)
led2 = Pin(27, Pin.OUT)

while True:

    if button.value() == True:
        print ("Button is pushed.")
        led1.on()
        led2.off()
    else:
        print ("Button is not pushed.")
        led1.off()
        led2.on()
    sleep(0.1)