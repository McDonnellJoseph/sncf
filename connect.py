from os import set_blocking
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import train_request
from bs4 import BeautifulSoup
import datetime
import pandas as pd 

class Search():
    """Class to initalize a search 
    """
    def __init__(self):
        """ connects to homepage
        """
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
        """
        function to launch a search but nothings happens when click on submit button

        Args:
            departure ([type]): [description]
            arrival ([type]): [description]
        """
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

    def result(self,dep,arv,date):
        """
        concatenates results and returns correct html with selenium 

        Args:
            dep ([type]): [description]
            arv ([type]): [description]
            date ([type]): [description]
        """
        url = train_request.make_url(dep, arv, date)
        self.browser.get(url)
        time.sleep(2)


        #plus tard 
    

    def next(self):
        self.browser.find_element_by_xpath('//button[@class="_il2jaxd"]').click()
    
    def extract(self):
        return self.browser.page_source


class Extractor():
    """
    Extracts information from the html given as input
    """

    def __init__(self, page):

        self.soup = BeautifulSoup(page)

        self.times = self.soup.find_all("div", { "class" : "_19sm4pk" })

        self.prices = self.soup.find_all("div", { "class" : "_m3zemr" })

    def make_lines(self):
        time_dep = []
        time_arv = []
        price_1 = []
        price_2 = []

        content = []

        assert len(self.times) == len(self.prices)

          

        for i in range(len(self.times)):
            print(self.times[i], self.prices[i])
            time_dep.append(self.times[i].text[:5])
            time_arv.append(self.times[i].text[5:]) 

            #extract prices
            prices = [word for word in self.prices[i].text.split()]

            prices = [price.strip('€') for price in prices]

            prices = [price.strip('cher') for price in prices]

            price_dep = True
            price_arv = True
            
            for price in prices:
                if len(price)==5:
                    if price_dep == True:
                        price_dep = False
                        price_1.append(price)
                    else:
                        price_2.append(price)
                        break
            if price_dep:
                price_1.append('Na')
            if price_arv:
                price_2.append('Na')


                                            

            

        
            

        return time_dep, time_arv, price_1, price_2



def generate_dates(k):
    """
    Generating k dates starting from today 

    Args:
        k ([type]): [description]

    Returns:
        [type]: [description]
    """
    initial = datetime.date.today()

    res = [initial + datetime.timedelta(days=idx) for idx in range(k)]

    return res 

        



if __name__ == '__main__':
    # initializing a browser object
    search = Search() 


    # create a range of dates from today :
    dates = generate_dates(5)
    #for each date 
    for date in dates:
        search.result('paris', 'lille', f"{date.year}-{date.month}-{date.day}")
        search.next()
        time.sleep(2)
        lala = search.extract()
        extract = Extractor(lala)
        val = extract.make_lines()
        data = {
            'date' : date,
            'date_dep' : val[0],
            'date_arv' : val[1],
            'price_1'  : val[2],
 
        }
        print(data)
        df = pd.DataFrame(data)
        df.to_csv('data/Paris_Lille.csv',sep=';',mode='a', index=False, header=False)





    


