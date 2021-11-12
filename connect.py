from os import set_blocking
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Search():
    """Class to initalize a search 
    """
    def __init__(self):
        #initialize driver
        self.browser = webdriver.Firefox()
        #access homepage 
        self.browser.get('https://www.trainline.fr/')
        self.body = self.browser.find_element_by_tag_name('body')
        time.sleep(2)
        #clicking through useless pop ups
        self.browser.find_element_by_id("onetrust-accept-btn-handler").click()
        time.sleep(1)
        self.browser.find_element_by_class_name('_1mw23jrNaN').click()

    def input(self, departure, arrival):
        #enter departure 
        departure_input = self.browser.find_element_by_id('from.search')
        departure_input.click()
        departure_input.send_keys(departure)
        departure_input.send_keys(Keys.ENTER)

        #enter arrival 
        arrival_input = self.browser.find_element_by_id('to.search')
        arrival_input.click()
        arrival_input.send_keys(arrival)
        arrival_input.send_keys(Keys.ENTER)

        #confirm
        confirm = self.browser.find_element_by_css_selector('div._mdez0w')
        confirm.click()

        


        pass

