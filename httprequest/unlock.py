import json
from constants.constants import Constants
import requests

class Http:

    def __init__(self):
        return

    def get(self, url, headers):
        response = requests.get(url, headers=headers)
        return response

    def post(self, url, headers, data):
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response

    def put(self):
        return bytes(self.toJSON(), "utf-8")
    
    def delete(self):
        return json.dumps(self.__dict__)