import os
from requests import get

def my_func():
    name = os.environ.get('name')
    response = get('http://www.google.com')
    return name, response.content
