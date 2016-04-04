import json


class NResponse(object):
    """
    Main Handler for all HTTP Responses
    """

    def __init__(self, http_version='', status='', headers={}, body=''):
        self.http_version = http_version
        self.headers = headers
        self.status = status
        self.body = body
        self.response = ''

    def encoded(self):
        self.response = self._generate_response(self.http_version,
                                                self.status,
                                                self.headers,
                                                self.body)
        return self.response.encode()

    def _generate_response(self, http_version, status, headers, body):
        base = "{0} {1}\r\n".format(http_version, status)
        for header in headers:
            base += "{0}: {1}\r\n".format(header, headers[header])
        # Also add custom headers (Server: Neptune)
        base += "\r\n"
        base += body

        return base

    def add_header(self, key, value):
        self.headers.update({'Set-Cookie': '{0}={1}'.format(key, value)})


class HTTPResponse(NResponse):
    """
    For HTTP Responses
    """

    def __init__(self, body, **kwargs):
        self.body = body
        # TODO: Defaults should be taken in a better way
        self.http_version = kwargs.get('http_version', 'HTTP/1.1')
        self.status = kwargs.get('status', '200 OK')
        self.headers = kwargs.get('headers', {})
        self.headers.update({'Server': 'Neptune'})
        super().__init__(http_version=self.http_version, status=self.status,
                         headers=self.headers, body=self.body)


class JSONResponse(HTTPResponse):
    """
    For sending JSON Responses
    """

    def __init__(self, body):
        # TODO: Raise error if body can't be json dumped
        super().__init__(json.dumps(body), headers={'Content-Type': 'application/json'})
