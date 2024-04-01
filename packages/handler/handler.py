import time
import logging

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
logger.propagate = True

class Handler:

    def __init__(self, Timers, Broadcaster, id):

        if not isinstance(Timers, list):
            raise TypeError('Timers must be tuple')
        
        if not isinstance(Broadcaster, object):
            raise TypeError('Broadcaster must be Type Object')
        
        self.Timers = Timers
        self.Broadcaster = Broadcaster
        self.id = id

        logger.debug(self.Timers)

    
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

                    message = {"id": self.id, "time": currentTime}
                    logger.debug(message)
                    self.Broadcaster.sendBroadcast(message)
