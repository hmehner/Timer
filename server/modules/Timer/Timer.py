import time

class Timer:
    
    def __init__(self, id, hours, minutes, seconds, finishAction=None):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.currentHours = None
        self.currentMinutes = None
        self.currentSeconds = None
        self.iteration = 0
        self.displayDuration = f'{hours:02}:{minutes:02}:{seconds:02}'

    def start(self):
        self.currentHours = self.hours
        self.currentMinutes = self.minutes
        self.currentSeconds = self.seconds

    def run(self):
        time.sleep(0.01)

        if self.seconds <= 0 and self.minutes > 0:
            self.minutes = self.minutes - 1
            self.seconds = 60

        if self.minutes <= 0 and self.hours > 0:
            self.hours = self.hours - 1
            self.minutes = 60

        self.seconds = self.seconds - 1
        self.iteration = self.iteration + 1
        
        self.displayDuration = f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
        return self.displayDuration
    
    def getIteration(self):
        return self.iteration