import random
from machine import Pin, PWM
from main import SimonGame
from time import sleep

game = SimonGame()

print ("Testing Pizeos")
print ("--------------")


#unit test - play tone
print ("Piezo 1")
game.play_tone(PWM(Pin(18)), 440, 1)
print ("Piezo 2")
game.play_tone(PWM(Pin(19)), 540, 1)
game.play_tone(PWM(Pin(20)), 640, 1)
game.play_tone(PWM(Pin(21)), 740, 1)

#unit tese - flash LED
game.flash_led(Pin(28, Pin.OUT), 1)
game.flash_led(Pin(27, Pin.OUT), 1)
game.flash_led(Pin(26, Pin.OUT), 1)
game.flash_led(Pin(22, Pin.OUT), 1)

game.all_leds_on()
sleep(1)
game.all_leds_off()

game.sequence.append(random.randint(0, 3))
game.sequence.append(random.randint(0, 3))
game.sequence.append(random.randint(0, 3))
game.sequence.append(random.randint(0, 3))
game.sequence.append(random.randint(0, 3))

game.play_sequence()

game.get_player_input()

print (game.player_sequence)

game.start_game()

game.stop_game()

game.cleanup()