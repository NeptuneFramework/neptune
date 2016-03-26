import socket
from neptune.handler import HTTPHandler
from neptune.response import HTTPResponse
from neptune.router import NRouter

class HelloWorld(object):
    def get(self):
        return HTTPResponse(http_version='HTTP/1.1', status="200 OK",
                       headers={'Content-Type': 'application/json', 'Server': 'Neptune'},
                       body='{"yash": "epicness"}').response



s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

port = 12345
s.bind(('', port))

res_obj = HTTPResponse(http_version='HTTP/1.1', status="200 OK",
                       headers={'Content-Type': 'application/json', 'Server': 'Neptune'},
                       body='{"yash": "epic"}')

router = NRouter()
router.add_rule('/', HelloWorld)

s.listen(3)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    data = c.recv(4096).decode()
    x = HTTPHandler(data)
    print(x.path)
    epic = router.get_cls(x.path)
    resp = getattr(epic, x.method.lower())()
    c.sendall(resp)
    c.close()
