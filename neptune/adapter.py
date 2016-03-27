from neptune.handler import HTTPHandler
from neptune.response import HTTPResponse
from neptune.router import NRouter

class NAdapter(object):
    """
    Bridges HTTPHandler, HTTPResponse and NRouter
    """

    def __init__(self):
        self.router = NRouter()

    def process_request(self, request):
        route = request.path
        method = request.method.lower()

        # TODO: Option to add decorators
        try:
            view_cls = self.router.get_cls(route)
            view_func = getattr(view_cls, method)
            return view_func()
        except Exception as e:
            print(str(e))
            raise(e)
