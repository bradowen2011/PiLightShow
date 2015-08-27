#title           : recorder.py
#author          : Brad Owen 
#date            : Aug 27 2015
#usage           : python recorder.py
#python_version  : 3.4.2  
#description     : play the music
#==============================================================================

import pygame
import time
import argparse
import Events

class Recorder:
    def __init__(self, musicPath, timeOffSet):
        pygame.mixer.init()
        pygame.mixer.music.load(musicPath)
        self.timeOffSet = timeOffSet
        pygame.display.set_mode((100, 100))

    def startMusic(self):
        pygame.mixer.music.play(start = self.timeOffSet)

    def recordEvents(self):
        startTime = time.time() - self.timeOffSet
        LightEvents = []
        while pygame.mixer.music.get_busy():
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    lightState = " ON  "
                elif event.type == pygame.KEYUP:
                    lightState = " OFF "
                else:
                    # we didn't catch an event we care about
                    break
                LightEvents.append("{0:.2f}".format(time.time() - startTime) + lightState + str(event.key) + "\n")

        with open('myfile','w') as outfile:
            for event in LightEvents:
                outfile.write(event)
        
    def startRecording(self):
        self.startMusic()
        self.recordEvents()

    def cleanup(self):
        pygame.mixer.quit()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-m", "--musicPath", type = str, help='', 
                   default='Music/Six_White_Boomers_-_A_Rolf_Harris_Tribute.mp3')
    p.add_argument("-t", "--timeToSkip", type = int, help='number of seconds to skip into the song', default=0)
    p.add_argument("-d", "--display", type = bool, help='display the light strands in a gui - see a light show with out hardware hooked up', default=0)
    args = p.parse_args()
    ls = Recorder(args.musicPath, args.timeToSkip)
    ls.startRecording()
    ls.cleanup()

