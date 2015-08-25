# import LightsPower
import LightsGuiOutput
import EventParser
import pygame
import argparse
import time

class LightShow:
    def __init__(self, piLightShowFile, timeOffSet):
        parser = EventParser.EventParser(piLightShowFile)
        self.events = parser.getEvents(timeOffSet)
        self.musicPath = parser.musicPath
        self.startTime = parser.startTime
        self.numberOfLightChannels = int(parser.numberOfLightChannels)
#         self.lights = LightsPower.PiLights()
        self.lights = LightsGuiOutput.PiLights(self.numberOfLightChannels)
        self.timeOffSet = timeOffSet
        
        pygame.mixer.init()
        pygame.mixer.music.load(self.musicPath)

    def displayEvents(self):
        for event in self.events:
            print('**********************')
            print('time stamp:', event.timeStamp)
            print('light state:', event.lightState)
            print('leds to modify:', event.leds)

    def startMusic(self):

        pygame.mixer.music.play(start = self.timeOffSet)

    def playEvents(self):
        # I observe about a .3 second delay between where i think the song should 
        # be in audacity, with what i hear
        offset = .3 # needs to be .3 for GPIO pins
        startTime = time.time() + offset - self.timeOffSet
        for event in self.events:
            # if positive, we need to wait that amount in seconds
            # if negative, we should have already run :D (sort to get around this?)
            whenToRun = startTime + float(event.timeStamp) - time.time()
            if whenToRun > 0:
                time.sleep(whenToRun)
            self.lights.change(event.lightState, event.leds)

    def playShow(self):
        self.startMusic()
        self.playEvents()

    def cleanup(self):
        pygame.mixer.quit()
        self.lights.cleanup()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-l", "--lightShowFile", type = str, help='', 
                   default='LightShowInstructions/sixWhiteBoomers.lsi')
    p.add_argument("-t", "--timeToSkip", type = int, help='number of seconds to skip into the song', default=0)
    p.add_argument("-d", "--display", type = bool, help='display the light strands in a gui - see a light show with out hardware hooked up', default=0)
    args = p.parse_args()
    ls = LightShow(args.lightShowFile, args.timeToSkip)
    ls.playShow()
    ls.cleanup()

