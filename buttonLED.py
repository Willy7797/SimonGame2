from machine import Pin
from time import sleep

button = Pin(14, Pin.IN) #2. 3. 4. 5. work, all LED work #start ans top button do  work
led1 = Pin(28, Pin.OUT)
led2 = Pin(27, Pin.OUT)
led3 = Pin(26, Pin.OUT)
led4 = Pin(22, Pin.OUT)

while True:

    if button.value() == True:
        print ("Button is pushed.")
        led1.off()
        led2.off()
        led3.on()
        led4.on()
    else:
        print ("Button is not pushed.")
        led1.on()
        led2.on()
        led3.off()
        led4.off()
    sleep(0.05)