class HTTPResponse(object):
    """
    Main Handler for all HTTP Responses
    """

    def __init__(self, http_version='', status='', headers={}, body=''):
        self.response = self._generate_response(http_ver, status, headers, body)

    def _generate_response(self, http_version, status, headers, body):
        base = "{0} {1}\r\n".format(http_ver, status)
        for header in headers:
            base += "{0}: {1}\r\n".format(header, headers[header])
        # Also add custom headers (Server: Neptune)
        base += "\r\n"
        base += body

        return base.encode()
