import unittest
import sys 
import os 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from connect import Search

class TestConnectionMethod(unittest.TestCase):

    def test_init(self):
        search = Search()
        assert search.browser.title
        
    def test_search(self):
        search = Search()
        print(search.input('Paris', 'Lille'))


if __name__ == '__main__':
    unittest.main()