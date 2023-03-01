import unittest
import os
import requests
import dummy_a
from ddt import ddt, data, unpack
from mock import patch, Mock, MagicMock
from dummy_a import my_func, get

mock_response = Mock()
mock_response.content = "...content"


@ddt
@patch.dict(os.environ, {"name": "patched"})
@patch('dummy_a.get', return_value=mock_response)
class TestDummyWorking(unittest.TestCase):
    def test_dummy(self, mock_get):
        name, content = my_func()
        print("name: {}".format(name))
        print("content: {}".format(content))


@ddt
@patch.dict(os.environ, {"name": "patched"})
@patch.object(dummy_a, get.__name__, return_value=mock_response)
class TestDummyWorking(unittest.TestCase):
    def test_dummy(self, mock_get):
        name, content = my_func()
        print("name: {}".format(name))
        print("content: {}".format(content))

