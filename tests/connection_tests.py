from datetime import time
import time
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
    
    def test_access(self):
        search = Search()
        search.result('paris','lille','2021-11-14')

    def test_access(self):
        search = Search()
        search.result('paris','lille', '2021-12-14')
        time.sleep(6)
        search.next()


if __name__ == '__main__':
    unittest.main()