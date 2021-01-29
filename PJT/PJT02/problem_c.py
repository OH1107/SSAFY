import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    my_key = '7ecf0fa910e1bacb146ddf503cf3ec72'
    url_make = URLMaker(my_key)
    url = url_make.get_url('movie','popular',region='KR',language='ko-KR')
    res = requests.get(url)
    popular_list = res.json()

    sorted_list = sorted(popular_list['results'], key=lambda x: x['vote_average'] ,reverse=True)
    top_5_title = sorted_list[:5]

    return top_5_title

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())