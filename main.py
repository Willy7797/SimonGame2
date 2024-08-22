from machine import Pin, PWM
import utime
import random

class SimonGame:
    def __init__(self):
        #Initialize GPIO pins
        self.led_pins = [Pin(28, Pin.OUT), Pin(27, Pin.OUT), Pin(26, Pin.OUT), Pin(22, Pin.OUT)]
        self.button_pins = [Pin(2, Pin.IN, Pin.PULL_DOWN), Pin(3, Pin.IN, Pin.PULL_DOWN), Pin(4, Pin.IN, Pin.PULL_DOWN), Pin(5, Pin.IN, Pin.PULL_DOWN)]
        self.speaker_pins = [PWM(Pin(18)), PWM(Pin(19)), PWM(Pin(20)), PWM(Pin(21))]
        self.start_switch = Pin(14, Pin.IN, Pin.PULL_DOWN)
        self.stop_switch = Pin(15, Pin.IN, Pin.PULL_DOWN)

        #Frequencies for the speakers corresponding to each LED
        self.tones = [440, 550, 660, 770]


        #Game state
        self.sequence = []
        self.player_sequence = []
        self.score = 0

    def play_tone(self):
        pass

    def flash_led(self):
        pass

    def play_sequence(self):
        pass

    def get_player_input(self):
        pass

    def start_game(self):
        pass

    def stop_game(self):
        pass

    def run(self):
        pass
    def cleanup(self):
        pass

game = SimonGame()
game.run()