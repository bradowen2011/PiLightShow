#the expected file format is as follows
#first line is path to the music to be played
#second line is what time to start the music
#third and on lines are events, with time from the start of the song to do the action, ON or OFF, then the strings to apply the change to.
# for example '1.05 ON 1 2 3' would turn on strings 1 2 and 3 1.05 seconds into the song
#use audacity to get your timing right
# this file must be in chronological order - if your timming is out of place, funny things will happen.  add error checking here


import Events

class EventParser:
    def __init__(self, fileName):
        self.events = []
        with open(fileName, 'r') as file:
            self.musicPath = file.readline().rstrip()
            self.startTime = file.readline().rstrip()
            for line in file.read().splitlines():
                line = line.split()
                #1st arg is the time stamp, 2nd the light state, and 3rd the light strings to modify
                self.events.append(Events.Events(line[0], line[1], line[2:]))

    def applyOffSet(self, timeOffSet):
        newEvents = []
        for event in self.events:
            if float(event.timeStamp) > timeOffSet:
                newEvents.append(event)
        self.events = newEvents

    def getEvents(self, timeOffSet):
        self.applyOffSet(timeOffSet)
        return self.events
