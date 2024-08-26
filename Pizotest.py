from machine import Pin, PWM
from time import sleep

buzzer1 = PWM(Pin(21))
buzzer2 = PWM(Pin(20))
buzzer3 = PWM(Pin(19))
buzzer4 = PWM(Pin(18))

buzzer1.freq(300) #set note
buzzer1.duty_u16(1000)#play100% volume
print("1done")
sleep(2)
buzzer1.duty_u16(0)#stop
#
buzzer2.freq(600) #set note
buzzer2.duty_u16(1000)#play100% volume
print("2done")
sleep(2)
buzzer2.duty_u16(0)#stop

#
buzzer3.freq(800) #set note
buzzer3.duty_u16(1000)#play100% volume
print("3done")
sleep(2)
buzzer3.duty_u16(0)#stop

#
buzzer4.freq(1000) #set note
buzzer4.duty_u16(1000)#play100% volume
print("4done")
sleep(2)
buzzer4.duty_u16(0)#stop