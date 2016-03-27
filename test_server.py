from neptune.server import NServer
from neptune.response import HTTPResponse

class HelloWorld(object):
    def get(self):
        return HTTPResponse(http_version='HTTP/1.1', status="200 OK",
                       headers={'Content-Type': 'application/json', 'Server': 'Neptune'},
                       body='{"yash": "epicness"}').response

app = NServer(port=5000)
app.router.add_rule('/', HelloWorld)

if __name__ == "__main__":
    app.run()
