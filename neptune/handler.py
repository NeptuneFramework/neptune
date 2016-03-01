class HTTPHandler(object):
    """
    Main Handler for parsing all HTTP Requests
    """

    def __init__(self, request):
        self.raw_request = request
        self.request_meta = request.split('\r\n\r\n', 1)[0].split('\r\n')
        self.request_data = request.split('\r\n\r\n', 1)[1]

        self.method, self.path, self.http_version = self.request_meta[0].split()
        self.headers_list = filter(None, self.request_meta[1:])
        self.headers = self._get_headers_dict(self.headers_list)

    def _get_headers_dict(self, headers_list):
        """
        Returns HTTP Headers in dictionary form
        """
        headers_dict = {}

        for header in headers_list:
            key, val = list(map(str.strip, header.split(':', 1)))
            headers_dict[key] = val
        return headers_dict
