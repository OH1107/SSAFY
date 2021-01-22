# PJT 01

## 00. 프로젝트 소개

> __Python을 활용한 데이터 수집__

### 1. 목표

- Python 기본 문법 실습
- 파일 입출력에 대한 이해
- 데이터 구조에 대한 분석과 이해
- 데이터를 가공하고 JSON 형태로 저장

### 2. 준비사항

- TMDB API (평점, 영화, 장르에 대한 API 서비스)
  - `genres.json`
    - 장르의 `id`, `name` 정보
  - `movie.json`
    - 샘플 영화의 정보
      - `adult`, `backdrop_path`, `genre_ids` 등 영화에 대한 간략한 정보
  - `movies.json`
    - 평점이 높은 20개의 영화데이터
      - 각 영화에 대한 `adult`, `backdrop_path`, `genre_ids` 등 간략한 정보
  - `.\movies\*.json`
    - 평점이 높은 20개의 영화에 대한 자세한 데이터
      - 20개의 `<영화_id>.json` 파일로 구성
      - `budget`, `revenue`, `relase_date` 등의 자세한 정보를 포함
- 개발언어 프로그램
  - Python 3.8 이상
- 필수 라이브러리
  - `json` , `os`

### 3. 요구사항

커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 데이터를 추출해 나가는 과정을 진행합니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다.

- [__A.__ 제공되는 영화 데이터의 주요내용 수집](https://github.com/OH1107/SSAFY/tree/main/PJT/PJT01#a-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EC%98%81%ED%99%94-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A3%BC%EC%9A%94%EB%82%B4%EC%9A%A9-%EC%88%98%EC%A7%91)

- [__B.__ 제공되는 영화 데이터의 주요내용 수정](https://github.com/OH1107/SSAFY/tree/main/PJT/PJT01#b-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EC%98%81%ED%99%94-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A3%BC%EC%9A%94%EB%82%B4%EC%9A%A9-%EC%88%98%EC%A7%91)
- [__C.__ 다중 데이터 분석 및 수정](https://github.com/OH1107/SSAFY/tree/main/PJT/PJT01#c-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EC%98%81%ED%99%94-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A3%BC%EC%9A%94%EB%82%B4%EC%9A%A9-%EC%88%98%EC%A7%91)
- [__D.__ 알고리즘을 통한 데이터 출력](https://github.com/OH1107/SSAFY/tree/main/PJT/PJT01#d-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%86%B5%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B6%9C%EB%A0%A5)
- [__E.__ 알고리즘을 통한 데이터 출력](https://github.com/OH1107/SSAFY/tree/main/PJT/PJT01#e-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%86%B5%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B6%9C%EB%A0%A5)



## 01. 프로젝트 내용

### A. 제공되는 영화 데이터의 주요내용 수집

> 샘플 영화데이터가 주어진다. 
>
> 이 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성한다.

#### 주요 코드 설명

서비스 구성에 필요한 정보는 다음과 같다.

```python
# 필요 데이터의 key 값
needs_list = ['id', 'title', 'poster_path', 
              'vote_average', 'overview', 'genre_ids',]
```

샘플 영화 데이터의 `dict` 데이터를 순회하며 필요한 데이터를 추출한다.

```python
# 결과를 입력할 변수 할당
result = {}
    
# 샘플 데이터를 순회
for item in movie.items():
	# 필요 데이터와 dict의 key값이 동일하다면
    if item[0] in needs_list:
        # 해당 데이터의 key와 value를 추출
        result[item[0]] = item[1]
```

#### :bulb: Point

- `for loop` 안에서 필요 데이터를 하나씩 대입하려고 하였다...
- 코드의 길이가 너무 길어지다 보니 `in` 예약어를 사용하였다.
  - '너가 찾는 key 값이 여기 리스트에 들어있니?' => 있으면 캐치 없으면 패스
- 가독성이 좋아지고 코드 길이도 짧아졌다. :clap:




### B. 제공되는 영화 데이터의 주요내용 수집

> 이전단계에서 만들었던 데이터를 활용하여, 
>
> `genre_ids`를 `genre_names`로 바꿔 반환하는 함수를 완성한다.

#### 주요 코드 설명

```python
    # 장르 이름을 받을 리스트 할당
    temp = []

    # genre.json 에서 id 번호 순회
    for genre in genres:
        # movie에서 받은 id 번호 순회
        for genre_id in result['genre_ids']:
            # movie에서 받은 id와 genre.json의 id가 서로 일치하다면
            if genre_id == genre['id']:
                # temp(장르 이름 보관하기 위한) 리스트에 할당
                temp.append(genre.get('name'))

    # for loop를 통해 찾은 value 값을 새로운 key에 부여
    result['genre_names'] = temp

    # 기존 'genre_ids' key 제거
    del(result['genre_ids'])
```

#### :bulb: Point

- 이중 `for loop` 를 사용했다...
- 해당 논리 이외에도 `for loop` 를 크게 2개를 돌리는 방법이 떠오르긴 했지만,,, 왠지 위의 코드가 더 짧지 않을까 했는데 도긴개긴인 듯하다.
- 오히려 이중 `for loop` 라 비효율적인 듯하다.



### C. 제공되는 영화 데이터의 주요내용 수집

> TMDB 기준 평점이 높은 20개의 영화 데이터가 있다. => `movies.json`
>
> 이 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성한다. 

#### 주요 코드 설명

먼저 20개 영화에 대한 정보를 `movie_results` 리스트에 할당하고자 했다.

> `movie_results = [{movie_01_info}, {movie_02_info}]`

```python
# 필요 데이터를 20개의 영화로부터 추출하기 위한 과정

# 필요 데이터의 key 값
needs_list = ['id', 'title', 'poster_path', 
              'vote_average', 'overview', 'genre_ids',]
    
# 전체 영화를 입력받을 리스트
movie_results = []

# 먼저 전체 영화 리스트를 순회하며 각각의 dict로 접근
for movie in movies:    
        
    # 영화별 필요한 데이터만을 할당할 dict
    result = {}
        
    # 각 영화의 dict에 접근하여 필요 데이터에 해당하는 key, value를 추출
    for item in movie.items():
        if item[0] in needs_list:
            result[item[0]] = item[1]

    # 전체 영화 리스트에 필요 데이터 dict를 추가
    movie_results.append(result)
```

20개의 영화 데이터를 모아놓은 `movie_results` 리스트를 돌며 __장르 이름__을 부여하고자 했다.

```python
# 추출한 20개의 영화데이터 중에서 ['genre_ids']를 ['genre_names']로 바꾸기 위한 과정

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
```



#### :bulb: Point

- 앞선 B 문제에서 이중 `for loop` 를 사용했기에 벌어진 참사다.
- 3중으로 `for loop` 를 사용했는데 가독성이 매우 떨어지고 본인조차도 코드를 짜며 헷갈렸다.
- 만일 `genres.json`으로 부터 `[{'id': 01, 'name': 'movie'}]` 형태의 리스트를 저장했다면, 본 문제에서는 이중 `for loop` 으로 해결할 수 있었을 것이다.... :sweat:



### D. 알고리즘을 통한 데이터 출력

> 세부적인 영화 정보 중 `수익 정보(revenue)` 를 이용하여 모든 영화 중 **가장 높은 수익을 낸 영화를 출력**하는 알고리즘을 작성한다.

#### 주요 코드 설명

`.\movies\` 에는 20개의 `*.json` 파일이 있다.

>  각 영화 `id` 값을 제목으로한 파일이다.

세부적인 정보를 포함한 데이터로, `movies.json` 에는 없는 `revenue` 에 대한 정보가 있다.

`revenue` 에 해당하는 영화 제목을 출력하기 위해서는

1. `*.json` 에서 모든 영화들 중 최고 `revenue` 를 판별
2. 해당 `revenue` 를 기록한 `id` 값을 찾아 `movies.json` 에서 비교
3. 동일한 `id` 값을 가진 영화의 `title` 을 반환

의 로직으로 구성했다.

~~(사실 세부 정보에도 영화 제목은 있으나, 함수에 대한 인자를 movies.json으로 받으니 id 값을 통해 출력하고자 했다.)~~

20개 파일을 하나의 리스트로 모아 편리하게 핸들링하기 위해 `os` 라이브러리를 사용했다.

```python
# 필요 라이브러리 호출
import os

# movies 폴더 안에 있는 모든 json 파일을 하나의 파일로 호출하는 과정

# 폴더의 경로
folderpath = r'data/movies'

# 파일의 경로(폴더 경로 + 파일 이름)으로 반복문을 리스트로 저장
filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

# 모든 json 파일을 모으기 위한 리스트
all_files = []

# 파일 경로 리스트를 순회하며
for path in filepaths:
    # 각 경로의 파일을 '읽기'로 'UTF8' 인코딩을 하여 열거야 라고 선언
    with open(path, 'r', encoding='UTF8') as f:
        # 해당 파일은 json 형태이므로 dict로 사용하기 위한 파싱
        file = json.load(f)
        # 호출된 파일을 모두 all_files 리스트에 저장
        all_files.append(file)
```

이제 20개 영화에 대한 세부정보를 모았다. 최고 `revenue` 값을 찾는 과정이다.

연습 문제에서 풀던 최대값 논리와 동일하다.

```python
# 최고 revenue 값과 해당 영화 id 판별
	
    # 대소비교를 위한 변수
	temp_rev = 0
    
    # 전체 세부정보 데이터를 순회하며
    for detail_info in all_files:
        
        # 각각의 수익정보 대소를 비교하는데, 나보다 더 큰 놈을 만나면
        if temp_rev <= detail_info['revenue']:
            # 수익정보를 임시 변수에 할당
            temp_rev = detail_info['revenue']
            # 큰 놈을 만났을때 해당 id도 temp_id에 저장
            temp_id = detail_info['id']
```

이제 해당 영화의 `id` 값을 찾았으니, `movies.json` 속에서 `id` 와 동일한 `title` 을 반환한다.

```python
	# 전체 영화를 순회하며
    for movie in movies:
        # 큰 놈을 만났을 때 저장한 id와 동일한 movie의 id를 만나면
        if temp_id == movie['id']:
            # 그 놈 타이틀을 반환해라
            return movie['title']
```

#### :bulb: Point

- `os` 라이브러리를 통해 다수의 파일을 읽는 방법을 검색하는데 오래걸렸다..
- 하나의 리스트로 다수의 파일을 입력받아 처리하니 훨씬 편리하다. :+1:



### E. 알고리즘을 통한 데이터 출력

> 세부적인 영화 정보 중 `개봉일 정보(release_date)` 를 이용하여 모든 영화 중 **12월에 개봉한 영화들의 리스트를 출력**하는 알고리즘을 작성한다.

#### 주요 코드 설명

D 문제와 거의 동일한 로직을 사용했다.

다수의 파일을 `os` 라이브러리를 사용해 불러왔고, (생략)

세부 데이터를 순회하며 조건에 맞는 데이터를 판별하는 과정이다.

```python
    # 영화 id를 임시적으로 받는 리스트
    temp_list = []
    
	# 세부 데이터 전체를 순회하며 개봉일을 조회
    for detail_info in all_files:
        # 개봉일 슬라이싱을 통해 월 자리만 추출, (2021-01-22일 경우 5번째 ~ 6번째가 월)
        # 그렇게 해서 만약 12월이라면
        if int(detail_info['release_date'][5:7]) == 12:
            # 해당 영화 id 값을 임시 리스트에 할당
            temp_list.append(detail_info['id'])
```

12월에 개봉한 영화들의 `id` 값을 모두 찾았으니, 

`movies.json` 에서 해당 `id` 값의 `title` 을 리스트로 모아주어 반환한다.

```python
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
```

#### :bulb: Point

- 12월에 해당하는 것을 어떻게 찾을까 하다가 __문자열 slicing__을 통해 추출할 수 있었다.
- D 문제와 많이 비슷하다 보니 금방 끝낼 수 있었다. :clap:

