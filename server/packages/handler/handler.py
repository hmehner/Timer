import time


class Handler:

    def __init__(self, Timers, Broadcaster):

        if not isinstance(Timers, list):
            raise TypeError('Timers must be tuple')
        
        if not isinstance(Broadcaster, object):
            raise TypeError('Broadcaster must be Type Object')
        
        self.Timers = Timers
        self.Broadcaster = Broadcaster

        print(self.Timers)

    
    """  
        Runs start method of workers
    """
    def startWorkers(self):

        for Timer in self.Timers:
            Timer.start()

        self.Broadcaster.start()


    """  
        Runs throug all the Timers 
    """
    def runTimers(self):
        
        time.sleep(1)
        for Timer in self.Timers:
            while not Timer.isFinished():
                if not Timer.getIsPaused():
                    currentTime = Timer.run(True)
                    print(currentTime)
                    self.Broadcaster.sendBroadcast(currentTime)
