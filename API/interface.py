import requests
# from Tools.Json_read import JsonRead


class InterfaceTest:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def interface_connect(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode('utf-8')

    def interface_response_status(self):
        status_code = requests.get(self.url)
        return status_code

    def interface_headers(self):
        response = requests.get(self.url)
        return response.headers
