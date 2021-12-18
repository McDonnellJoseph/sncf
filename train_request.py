import requests
import datetime
#attempt number2 by recreating destination url 
dic = {
    'paris': '69b59b70a73b72302eff45627aeef377',

    'lille': '902c76b31cbcf8632d9494013a98f63f',

    'bordeaux': '3a78b793b6015ef39d0cb9839c679e1a'

}


def make_url(dep, arv, date):
    """function to recreate correct trainline url 

    Args:
        dep ([type]): [description]
        arv ([type]): [description]
        date ([type]): [description]
    """
    payload = {'origin' : dic[dep], 'destination' :dic[arv], 'outwardDate':date }
    response = requests.get('https://www.thetrainline.com/book/results?', params=payload)
    return response.url

def make_dates(n):
    """Generate n dates after today's date 

    Args:
        n ([type]): [description]
    """
    


print(make_url('paris','lille', '2021-11-15'))