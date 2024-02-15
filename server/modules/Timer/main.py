import time
import Timer as t

hours = 0
minutes = 1
seconds = 5

myTimer = t.Timer(123, hours, minutes, seconds)

duration = hours * 3600 + minutes * 60 + seconds

startTime = time.time()
paused = False

myTimer.start()
while True:
    while paused == False:
        if myTimer.getIteration() < duration:
            time = myTimer.run()
            print(time)
        else:
            break


endTime = time.time()

print(endTime - startTime)
