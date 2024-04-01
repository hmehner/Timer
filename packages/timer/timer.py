import time
import logging

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
logger.propagate = True

class Timer:
    
    def __init__(self, hours, minutes, seconds, finishAction=None):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.currentHours = None
        self.currentMinutes = None
        self.currentSeconds = None
        self.iteration = 0
        self.currentDuration = {"hours": hours, "minutes": minutes, "seconds": seconds}
        self.isPaused = False

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

        beginTime = time.perf_counter()

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
        
        self.currentDuration = {"hours": self.currentHours, "minutes": self.currentMinutes, "seconds": self.currentSeconds}

        if debug == True:
            targetSleepTime = 0.01
        else:
            targetSleepTime = 1

        endTime = time.perf_counter()
        sleepTime = targetSleepTime - (endTime - beginTime)
        time.sleep(sleepTime)

        return self.currentDuration
    

    """  
        Sets paused State of Timer according to Input
    """
    def setPaused(self, isPaused):

        self.isPaused = isPaused

    """  
        Checks for paused State of Timer
    """
    def getIsPaused(self):

        return self.isPaused
    
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





"""  
    Module Functions
"""
def runTimer(name, hours, minutes, seconds, sendEvent):

    Broadcaster = Broadcaster("", 5555)
    
    
    # Initialize Timer with Values
    myTimer = Timer(name, hours, minutes, seconds, sendEvent)
    myTimer.start()
    paused = False

    # Loop for running timer and checking pause-state
    while paused == False:
        if myTimer.isFinished() == False:
            time = myTimer.run()
            print(time)
        else:
            break