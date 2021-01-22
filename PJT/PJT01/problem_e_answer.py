import json
import os

def dec_movies(movies):
    # 여기에 코드를 작성합니다.

    # movies 폴더 안에 있는 모든 세부데이터.json 파일을 하나의 파일로 호출하는 과정
    folderpath = r'data/movies'
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    all_files = []

    for path in filepaths:
        with open(path, 'r', encoding='UTF8') as f:
            file = json.load(f)
            all_files.append(file)
    
    # 영화 id를 임시적으로 받는 리스트
    temp_list = []
    
    # 세부 데이터 전체를 순회하며 개봉일을 조회
    for detail_info in all_files:
        # 개봉일 슬라이싱을 통해 월 자리만 추출, 만약 12와 같다면
        if int(detail_info['release_date'][5:7]) == 12:
            # 해당 영화 id 값을 임시 리스트에 할당
            temp_list.append(detail_info['id'])
    
    # 영화 제목을 받을 리스트
    movie_list = []

    # 전체 영화 데이터를 순회
    for movie in movies:
        # 12월에 개봉한 영화 id 리스트 순회
        for id_num in temp_list:
            # 12월 개봉 영화 id와 전체 영화 데이터중 id가 동일하면
            if id_num == movie['id']:
                # 해당 영화 제목을 리스트에 할당
                movie_list.append(movie['title'])

    return movie_list
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))