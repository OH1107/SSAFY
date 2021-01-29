import requests
from pprint import pprint
from tmdb import URLMaker


def popular_count():
    my_key = '7ecf0fa910e1bacb146ddf503cf3ec72'
    url_make = URLMaker(my_key)
    url = url_make.get_url('movie','popular',region='KR',language='ko-KR')
    res = requests.get(url)
    popular_list = res.json()
    
    pop_count = len(popular_list['results'])
    
    return pop_count



if __name__ == '__main__':
    pprint(popular_count())