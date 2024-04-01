import socket
import threading
import logging

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
logger.propagate = True

class Broadcaster():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.serverAddress = (host, port)
        self.clients = []
        self.eventSend = threading.Event()

    """  
        Starts the handler for sending messages. 
        Waits for incoming connctions and stores them. 
    """
    def start(self):
        self.broadcastServer  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.broadcastServer.bind(self.serverAddress)
        self.broadcastServer.listen()

        self.broadcastingHandler = threading.Thread(target=self.handleBroadcasting)
        self.broadcastingHandler.start()

        self.requestHandler = threading.Thread(target=self.handleRequests)
        self.requestHandler.start()

        logger.info('Started Handler succesfully!')

    def handle_message(self):
        while True:
                clientSocket, address = self.broadcastServer.accept()
                print(f'Received new Connection: {clientSocket}, {address}')
                self.clients.append(clientSocket)

    """  
        Waits for threading event for sending Broadcast.
        When received, extract data for Broadcast and sends one.
    """
    def handleBroadcasting(self):
        while True:
            self.eventSend.wait()
            print('Received event Send')
            data = 'test'
            self.sendBroadcast(data)
            self.eventSend.clear()
            print('Cleared event Send')

    """  
        Sends a Socket message to all clients subscribed to the Broadcaster Socket
    """
    def sendBroadcast(self, message):

        if self.clients:
            for clientSocket in self.clients:
                try:
                    clientSocket.send(message.encode())
                    logger.debug(f'Sent data: {message}')
                except Exception as e:
                    logger.warning(f"Error broadcasting message: {e}")
        else:
            logger.debug('Tried to send data, but no connections available')


    def getEvent(self):
        return self.eventSend