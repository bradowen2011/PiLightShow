import RPi.GPIO
import time

class PiLights:
    def __init__(self):
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setwarnings(False)

        #match the led color with the pin on the GPIO
        self.blue = 4
        self.red = 17
        self.yellow = 12
        self.green = 16

        self.allLeds = [self.blue, self.red, self.green, self.yellow]

        RPi.GPIO.setup(self.blue, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.red, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.yellow, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.green, RPi.GPIO.OUT)

    def cleanup(self):
        RPi.GPIO.cleanup()

    def turnAllOn(self):
        for led in self.allLeds:
            RPi.GPIO.output(led, 1)

    def turnAllOff(self):
        for led in self.allLeds:
            RPi.GPIO.output(led, 0)

    def flashAll(self, iterations, wait):
        for i in range(0, iterations):
            self.turnAllOn()
            time.sleep(wait)
            self.turnAllOff()
            time.sleep(wait)

    def circleChase(self, iterations, wait):
        for i in range(0, iterations):
            previousLed = self.allLeds[-1]
            RPi.GPIO.output(previousLed, 1)
            for led in self.allLeds:
                RPi.GPIO.output(previousLed, 0)
                RPi.GPIO.output(led, 1)
                previousLed = led
                time.sleep(wait)
        self.turnAllOff()

    def change(self, state, leds):
        pinState = 0
        if state.lower() == 'on':
            pinState = 1
        for led in leds:
            RPi.GPIO.output(self.allLeds[int(led) - 1], pinState)


if __name__ == "__main__":
    pl = PiLights()
    #pl.flashAll(10, .1)
    pl.circleChase(10, .1)
    pl.cleanup()
