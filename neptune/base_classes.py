from neptune.response import HTTPResponse

class Error404(object):
    def get(self):
        return HTTPResponse('404 Not Found Error', status="404 Not Found")
