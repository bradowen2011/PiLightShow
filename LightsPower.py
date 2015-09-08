import RPi.GPIO
import time

class LightsPower:
    def __init__(self):
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setwarnings(False)

        #match the led color with the pin on the GPIO
        blue = 4
        red = 17
        yellow = 12
        green = 16

        self.allChannels = [blue, red, green, yellow]

        RPi.GPIO.setup(blue, RPi.GPIO.OUT)
        RPi.GPIO.setup(red, RPi.GPIO.OUT)
        RPi.GPIO.setup(yellow, RPi.GPIO.OUT)
        RPi.GPIO.setup(green, RPi.GPIO.OUT)

    def cleanup(self):
        RPi.GPIO.cleanup()

    def turnAllOn(self):
        for led in self.allChannels:
            RPi.GPIO.output(led, 1)

    def turnAllOff(self):
        for led in self.allChannels:
            RPi.GPIO.output(led, 0)

#     def flashAll(self, iterations, wait):
#         for i in range(0, iterations):
#             self.turnAllOn()
#             time.sleep(wait)
#             self.turnAllOff()
#             time.sleep(wait)

#     def circleChase(self, iterations, wait):
#         for i in range(0, iterations):
#             previousLed = self.allChannels[-1]
#             RPi.GPIO.output(previousLed, 1)
#             for led in self.allChannels:
#                 RPi.GPIO.output(previousLed, 0)
#                 RPi.GPIO.output(led, 1)
#                 previousLed = led
#                 time.sleep(wait)
#         self.turnAllOff()

    def change(self, state, leds):
        pinState = 0
        if state.lower() == 'on':
            pinState = 1
        for led in leds:
            RPi.GPIO.output(self.allChannels[int(led) - 1], pinState)


if __name__ == "__main__":
    pl = LightsPower()
    #pl.flashAll(10, .1)
    pl.circleChase(10, .1)
    pl.cleanup()
