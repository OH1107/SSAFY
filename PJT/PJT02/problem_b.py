import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    my_key = '7ecf0fa910e1bacb146ddf503cf3ec72'
    url_make = URLMaker(my_key)
    url = url_make.get_url('movie','popular',region='KR',language='ko-KR')
    res = requests.get(url)
    popular_list = res.json()

    result_list = []
    for movie in popular_list['results']:
        if movie['vote_average'] >= 8:
            result_list.append(movie)

    return result_list

if __name__ == '__main__':
    pprint(vote_average_movies())    
