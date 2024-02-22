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
        self.currentDuration = f'{hours:02}:{minutes:02}:{seconds:02}'

    """  
        Sets calculation Values
    """
    def start(self):

        # updating Values
        self.currentHours = self.hours
        self.currentMinutes = self.minutes
        self.currentSeconds = self.seconds
        self.maxIterations = self.hours * 3600 + self.minutes * 60 + self.seconds


    """ 
        Executes one iteration of the timer.
        Sleep time is dynamicly calculated.
        debug = True/False  speeds up timer iteration substantially 
    """
    def run(self, debug = False):

        beginTime = time.time()

        # Calculation for new hour
        if self.currentMinutes <= 0 and self.currentSeconds <= 0 and self.currentHours > 0:
            self.currentHours = self.currentHours - 1
            self.currentMinutes = 60

        # Calculation for new Minute
        if self.currentSeconds <= 0 and self.currentMinutes > 0:
            self.currentMinutes = self.currentMinutes - 1
            self.currentSeconds = 60

        self.currentSeconds = self.currentSeconds - 1
        self.iteration = self.iteration + 1
        
        self.currentDuration = f'{self.currentHours:02}:{self.currentMinutes:02}:{self.currentSeconds:02}'

        if debug == True:
            targetSleepTime = 0.01
        else:
            targetSleepTime = 1

        endTime = time.time()

        sleepTime = targetSleepTime - (endTime - beginTime)

        print(sleepTime)
        print(self.iteration)
        time.sleep(sleepTime)
        return self.currentDuration

    
    def getIteration(self):
        return self.iteration
    
    """
        Checks if Timer should be stopped  
    """
    def isFinished(self):
        
        # Checking if maxIteration is reached
        return self.iteration >= self.maxIterations
    
    """
        Reset calculating Values back to default  
    """
    def reset(self):

        # Setting Values
        self.currentSeconds = self.seconds
        self.currentMinutes = self.minutes
        self.currentHours = self.hours
        self.iteration = 0