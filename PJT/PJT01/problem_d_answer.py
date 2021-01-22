import json
import os

def max_revenue(movies):
    # 여기에 코드를 작성합니다.

    # movies 폴더 안에 있는 모든 json 파일을 하나의 파일로 호출하는 과정
    folderpath = r'data/movies'
    filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    all_files = []

    for path in filepaths:
        with open(path, 'r', encoding='UTF8') as f:
            file = json.load(f)
            all_files.append(file)
    
    # 최고 revenue 값과 해당 영화 id 출력
    temp_rev = 0
    for detail_info in all_files:
        if temp_rev <= detail_info['revenue']:
            temp_rev = detail_info['revenue']
            temp_id = detail_info['id']

    for movie in movies:
        if temp_id == movie['id']:
            return movie['title']

    # for 문으로 json 파일 죄다 호출
    # revenue 비교하면서 임시에다가 최대 값이랑 최대값 id 저장
    # 해당 레비뉴 값의 영화 id가지고 movies.json에서 검색
    # 영화 제목 출력
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))