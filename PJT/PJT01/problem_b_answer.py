import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.

    # 필요 데이터의 key 값
    needs_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    
    # 결과를 입력할 변수 할당
    result = {}
    
    # 입력 데이터를 순회하며 필요 데이터에 해당하는 key, value를 추출
    for item in movie.items():
        if item[0] in needs_list:
            result[item[0]] = item[1]
    
    # 장르 이름을 받을 리스트 할당
    temp = []

    # genre.json 에서 id 번호 순회
    for genre in genres:
        # movie에서 받은 id 번호 순회
        for genre_id in result['genre_ids']:
            # 만약 id 번호가 서로 일치하다면
            if genre_id == genre['id']:
                temp.append(genre.get('name'))

    # for loop를 통해 찾은 value 값을 새로운 key에 부여
    result['genre_names'] = temp

    # 기존 'genre_ids' key 제거
    del(result['genre_ids'])

    return result
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))