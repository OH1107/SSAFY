import json
from pprint import pprint


def movie_info(movie):
    # 여기에 코드를 작성합니다.

    # 필요 데이터의 key 값
    needs_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    
    # 결과를 입력할 변수 할당
    result = {}
    
    # 입력 데이터를 순회하며 필요 데이터에 해당하는 key, value를 추출
    for item in movie.items():
        if item[0] in needs_list:
            result[item[0]] = item[1]
    
    return result
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json) # python dict 형태로 변환
    
    pprint(movie_info(movie_dict))