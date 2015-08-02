import LED
import EventParser
import pygame
import time
import argparse

class LightShow:
    def __init__(self, piLightShowFile, timeOffSet):
        parser = EventParser.EventParser(piLightShowFile)
        self.events = parser.getEvents(timeOffSet)
        self.musicPath = parser.musicPath
        self.startTime = parser.startTime
        self.lights = LED.PiLights()
        self.timeOffSet = timeOffSet

    def displayEvents(self):
        for event in self.events:
            print('**********************')
            print('time stamp:', event.timeStamp)
            print('light state:', event.lightState)
            print('leds to modify:', event.leds)

    def startMusic(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.musicPath)
        pygame.mixer.music.play(start = int(self.startTime) + self.timeOffSet)

    def playEvents(self):
        # I observe about a .3 second delay between where i think the song should 
        # be in audacity, with what i hear
        offset = .3
        startTime = time.time() + offset - self.timeOffSet
        for event in self.events:
            # if positive, we need to wait that amount in seconds
            # if negative, we should have already run :D
            whenToRun = startTime + float(event.timeStamp) - time.time()
            if whenToRun > 0:
                time.sleep(whenToRun)
            self.lights.change(event.lightState, event.leds)
            print(event.lightState, event.leds)

    def playShow(self):
        self.startMusic()
        self.playEvents()

    def cleanup(self):
        self.lights.cleanup()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-t", "--timeToSkip", type = int, help='number of seconds to skip into the song', default=0)
    args = p.parse_args()
    ls = LightShow('saintsGoMarching.pls', args.timeToSkip)
    ls.playShow()
    ls.cleanup()
