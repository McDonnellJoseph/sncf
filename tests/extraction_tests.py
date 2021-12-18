from datetime import time
import time
import unittest
import sys 
import os 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from connect import Search
from connect import Extractor


class TestExtraction(unittest.TestCase):
    def test_html(self):
        search = Search()
        search.result('paris','lille', '2021-12-14')
        time.sleep(2)
        search.next()
        time.sleep(3)
        search.next()
        time.sleep(3)
        extract = Extractor(search.extract())
        extract.make_lines()
        
    




if __name__=='__main__':
    unittest.main()