import socket
from protocol import Serializer

class MongoClient:
    def __init__(self, host = '127.0.0.1', port = 1234):
        self.host = host
        self.port = port

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((host, port))
        # TO DO !

        self._parser = None

    def send_command(self, args*) -> any:
        """
        Send command and wait for response.
        """
        command = Serializer.encode(args)







