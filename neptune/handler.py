from urllib.parse import parse_qs, urlparse


class NRequest(object):
    """
    Main Handler for parsing all HTTP Requests
    """

    def __init__(self, request):
        self.raw_request = request
        self.request_meta = request.split('\r\n\r\n', 1)[0].split('\r\n')
        self.request_data = request.split('\r\n\r\n', 1)[1]

        self.method, self.url, self.http_version = self.request_meta[0].split()
        self.headers_list = filter(None, self.request_meta[1:])

        self.route = urlparse(self.url).path
        self.params = self._get_request_params(self.url)
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

    def _get_request_params(self, url):
        """
        Returns Request Parameters as a dict
        """

        parsed_url = urlparse(url)
        parsed_params = parse_qs(parsed_url.query)
        parsed_params = {key:parsed_params[key][0] for key in parsed_params}
        return parsed_params
