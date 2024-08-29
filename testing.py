import random
from machine import Pin, PWM
from main import SimonGame
from time import sleep

game = SimonGame()


#unit test - play tone
print ("Testing Pizeos")
print ("--------------")
print ("Piezo 1")
game.play_tone(PWM(Pin(18)), 440, 1)
print ("Piezo 2")
game.play_tone(PWM(Pin(19)), 540, 1)
print ("Piezo 3")
game.play_tone(PWM(Pin(20)), 640, 1)
print ("Piezo 4")
game.play_tone(PWM(Pin(21)), 740, 1)

#unit test - flash LED
print ("Testing LED")
print ("------------")
print("LED 1")
game.flash_led(Pin(28, Pin.OUT), 1)
print("LED 2")
game.flash_led(Pin(27, Pin.OUT), 1)
print("LED 3")
game.flash_led(Pin(26, Pin.OUT), 1)
print("LED 4")
game.flash_led(Pin(22, Pin.OUT), 1)

#unit test - LED on and off
print ("Testing LED on/off")
print ("------------------")
print("LED on")
game.all_leds_on()
sleep(1)
print("LED ff")
game.all_leds_off()

#unit test - sequence
print ("Testing Sequunce")
print ("----------------")
game.sequence.append(random.randint(0, 3))
game.sequence.append(random.randint(0, 3))
game.sequence.append(random.randint(0, 3))
game.sequence.append(random.randint(0, 3))
game.sequence.append(random.randint(0, 3))

#unit test - play sequence
print ("Testing Play Sequence")
print ("------------------")
game.play_sequence()

#unit test - Player Input
print ("Testing Play Input")
print ("------------------")
game.get_player_input()
print (game.player_sequence)

#Unit Test - Start Game
print ("Testing Start Game")
print ("------------------")
game.start_game()

#Unit Test - Stop Game
print ("Testing Stop Game")
print ("-----------------")
game.stop_game()

#Unit Test - Cleanup
print ("Testing Cleanup")
print ("---------------")
game.cleanup()