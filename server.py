import socket
from neptune.handler import HTTPHandler
from neptune.response import HTTPResponse

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

port = 12345
s.bind(('', port))

res_obj = HTTPResponse(http_version='HTTP/1.1', status="200 OK",
                       headers={'Content-Type': 'application/json', 'Server': 'Neptune'},
                       body='{"yash": "epic"}')


s.listen(3)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    data = c.recv(4096).decode()
    x = HTTPHandler(data)
    print("Method: " + x.method)
    print(x.headers)
    print(x.http_version)
    print(x.path)
    print(x.method)
    print(x.request_data)
    c.sendall(res_obj.response)
    c.close()     
