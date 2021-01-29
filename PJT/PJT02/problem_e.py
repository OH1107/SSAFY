import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    my_key = '7ecf0fa910e1bacb146ddf503cf3ec72'
    url_make = URLMaker(my_key)
    id_num = url_make.movie_id(title)
    
    if id_num == None:
        return None

    url = url_make.get_url(category='movie', feature=f'{id_num}/credits', language='ko-KR')
    res = requests.get(url)
    credit_list = res.json()

    cast_list = [info['name'] for info in credit_list['cast'] if info['cast_id'] <= 10]
    crew_list = [info['name'] for info in credit_list['crew'] if info['department'] == 'Directing']
    
    credits_result = {'cast': cast_list, 'crew': crew_list}
    
    return credits_result

if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None