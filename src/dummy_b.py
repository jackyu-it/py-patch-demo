import os
import requests


def my_func():
    name = os.environ.get('name')
    response = requests.get('http://www.google.com')
    return name, response.content
