import unittest
import sys 
import os 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import train_request


class TestRequestMethod(unittest.TestCase):
    def test_request(self):
        assert train_request.make_url('paris','lille','2021-11-13',12) == 200



if __name__ == '__main__':
    unittest.main()