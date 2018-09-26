import requests
from flask import session

class SwaggerData:

    def __init__(self, url):
        self.url = url

    def get_json_data(self):
        r = requests.get(self.url, {'token': session['access_token']})

        return r






