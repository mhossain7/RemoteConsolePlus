'''Created by Dmytro Konobrytskyi, 2012(C)'''

import zmq
from RCPServer.ConfigManager.ConfigManager import NetworkConfig

class Server(object):
    '''Server is used for receiving messages over network from clients'''

    def __init__(self, inputRouter):
        self._inputRouter = inputRouter

        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)
        self._socket.bind(NetworkConfig.NetworkAddress)
        self._socket.setsockopt(zmq.SUBSCRIBE, "")
        
    def ReceiveMessages(self):
        message = "test"
        self._inputRouter.PassMessage(message)