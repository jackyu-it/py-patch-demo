import unittest
import os
import requests
from ddt import ddt, data, unpack
from mock import patch, Mock, MagicMock
from dummy_b import my_func


mock_response = Mock()
mock_response.content = "...content"


@ddt
@patch.dict(os.environ, {"name": "patched"})
@patch.object(requests, requests.get.__name__, return_value=mock_response)
class TestDummy(unittest.TestCase):
    def test_dummy(self, mock_get):
        name, content = my_func()
        print("name: {}".format(name))
        print("content: {}".format(content))