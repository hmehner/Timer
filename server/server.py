from flask import Flask, jsonify
from flask_cors import CORS
import threading

from packages.timer import Timer
from packages.broadcaster import Broadcaster
from packages.handler import Handler


app = Flask(__name__)
CORS(app)


@app.route('/get-timers', methods=['GET'] )
def getTimers():

    print('Requested timers')

    data = [
    {
        'name': 'Timer1',
        'hours': 2,
        'minutes': 1,
        'seconds': 3
    },
    {
        'name': 'Waky Waky',
        'hours': 1,
        'minutes': 15,
        'seconds': 59
    }
]

    return jsonify(data)


@app.route('/start-timer', methods=['POST'])
def startTimer():

    # Creating Timers
    timer1 = Timer(0, 1, 6)
    timer2 = Timer(1, 2, 3)
    timers = [timer1, timer2]

    # Creating Broadcaster for Socket Transmition of time
    myBroadcaster = Broadcaster('', 5432)

    # Create Handler
    myHandler = Handler(timers, myBroadcaster)
    myHandler.startWorkers()

    handlerThread = threading.Thread(target=myHandler.runTimers)
    handlerThread.start()

    data = {
        'message': 'Timers started'
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)