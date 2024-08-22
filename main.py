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

    def play_tone(self, speaker, tone, duration):
        speaker.freq(tone)
        speaker.duty_u16(32768)
        utime.sleep(duration)
        speaker.duty_u16(0)

    def flash_led(self, led, duration):
        led.on()
        utime.sleep(duration)
        led.off()

    def play_sequence(self):
        for i in self.sequence:
            self.flash_led(self.led_pins[i], 0.5)
            self.play_tone(self.speaker_pins[i], self.tones[i], 0.5)
            utime.sleep(0.2)

    def get_player_input(self):
           self.player_sequence = []
           for _ in range(len(self.sequence)):
               while True:
                   for i, button in enumerate(self.button_pins):
                       if button.value() == 1:
                           self.flash_led(self.led_pins[i], 0.5)
                           self.play_tone(self.speaker_pins[i], self.tones[i], 0.5)
                           self.player_sequence.append(i)
                           utime.sleep(0.5)
                           break
                   else:
                       continue
                   break

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