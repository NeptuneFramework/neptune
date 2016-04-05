import datetime
from neptune.server import NServer
from neptune.response import JSONResponse, HTTPResponse

key = "2"
data = "username"
date = datetime.datetime.now()


class HelloWorld(object):
    def get(self):
        app.session.initialize_session(key,data)
        xyz = JSONResponse({"hello": "world", "numbers": [1,2,3,4,5]})
        return xyz

class ByeWorld(object):
    def get(self):
        try:
        	sess_id = self.request.cookies['session_id']
        	print(app.session.get_value(key, sess_id))
        except Exception as e:
        	print(str(e))
        abc = HTTPResponse("Bye World")
        return abc

app = NServer(port=5000)
app.router.add_rule('/', HelloWorld)
app.router.add_rule('/yash', ByeWorld)

if __name__ == "__main__":
    app.run()
