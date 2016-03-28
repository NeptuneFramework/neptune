from socket import (
    AF_INET,
    SOCK_STREAM,
    socket
)

from neptune.handler import HTTPHandler
from neptune.adapter import NAdapter
from neptune.router import NRouter


class NServer(object):
    """
    Neptune Server
    """

    def __init__(self, host='', port=7500):
        self.nsocket = socket(AF_INET, SOCK_STREAM)
        self.host = host
        self.port = port
        self.nsocket.bind((self.host, self.port))
        # TODO: listen here or in run
        self.nsocket.listen(3)
        self.router = NRouter()

    def _process_request(self, request):
        route = request.path
        method = request.method.lower()

        # TODO: Option to add decorators
        try:
            view_cls = self.router.get_cls(route)
            view_func = getattr(view_cls, method)
            return view_func()
        except Exception as e:
            print(str(e))
 

    def run(self):
        """
        The run hanlder
        """
        print('Listening on port {}'.format(self.port))
        while True:
            connection, address = self.nsocket.accept()
            print('Got connection from ', address)  # Move it to if self.debug

            data_recv = connection.recv(4096).decode()  # why 4096 ? Think of better variable name too
            request = HTTPHandler(data_recv)

            response = self._process_request(request)
            connection.sendall(response.encoded())
            connection.close()
