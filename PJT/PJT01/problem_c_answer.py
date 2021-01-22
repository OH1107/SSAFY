import json
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.

    # 지정 데이터만 호출하기 위한 과정

    # 필요 데이터의 key 값
    needs_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    
    # 전체 영화를 입력받을 리스트 할당
    movie_results = []

    # 먼저 전체 영화 리스트를 순회하며 각각의 dict로 접근
    for movie in movies:    
        
        # 영화별 dict를 입력할 변수 할당
        result = {}
        
        # 각 영화의 dict에 접근하여 필요 데이터에 해당하는 key, value를 추출
        for item in movie.items():
            if item[0] in needs_list:
                result[item[0]] = item[1]

        # 전체 영화 리스트에 필요 데이터 dict를 추가
        movie_results.append(result)

    # genre_ids => genre_names를 위한 과정

    # 영화 데이터를 모아놓은 movie_results 리스트를 순회
    for movie in movie_results:

        # 장르 이름을 받을 임시 리스트 할당
        temp = []

        # 리스트 속의 영화 정보 데이터 dict 중 'genre_ids' 속의 데이터를 순회
        for genre_id in movie['genre_ids']:

            # genres.json 파일 안의 genre 데이터 순회
            for genre in genres:
                # 영화의 genre_id값이 genres.json안에 genre의 id 값과 같으면
                if genre_id == genre['id']:
                    # 해당 dict의 name에 대한 value를 임시 리스트에 할당
                    temp.append(genre.get('name'))
        # 다음 루프(영화)로 넘어가기 전 영화에 해당 장르 이름을 부여
        movie['genre_names'] = temp

        # 장르 이름 할당을 마친 후, id 값은 제거
        del(movie['genre_ids'])

    return movie_results
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))