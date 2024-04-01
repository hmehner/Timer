from fastapi import FastAPI, BackgroundTasks, WebSocket
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

import threading
import logging.config
import os
import yaml

from packages.timer import Timer
from packages.broadcaster import Broadcaster
from packages.handler import Handler


logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
logger.propagate = True
logger.info("info message")

configFile = f"{os.path.dirname(os.path.abspath(__file__))}/config/logger.yml"
with open(configFile) as file:
    logger.debug(f'{file}')
    config = yaml.safe_load(file)
    logging.config.dictConfig(config)


app = FastAPI()

websocket_connections = []

@app.websocket("/websockets/timers")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    # Add Connection to list for access later
    websocket_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Senden der Nachricht an alle verbundenen Clients
            for connection in websocket_connections:
                await connection.send_text(data)
    except:
        logger.warning('Error')

@app.get('/get-timers')
async def getTimers():

    logger.info('Received an API Request for getting timers')

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

    return jsonable_encoder(data)


@app.post('/start-timer')
async def startTimer(backgroundTask: BackgroundTasks):
    
    logger.info('Received API Request for starting Timer')

    # Creating Timers
    timer1 = Timer(0, 1, 6)
    timer2 = Timer(1, 2, 3)
    timers = [timer1, timer2]

    # Creating Broadcaster for Socket Transmition of time
    myBroadcaster = Broadcaster('', 5432)

    # Create Handler
    myHandler = Handler(timers, myBroadcaster, 1234567)
    myHandler.startWorkers()

    backgroundTask.add_task(threading.Thread(target=myHandler.runTimers).start)
    logger.info('Started Thread for Handler')

    data = {
        'message': 'Timers started'
    }
    return jsonable_encoder(data)