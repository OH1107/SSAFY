# PJT 02

## 00. 프로젝트 소개

> Python을 활용한 데이터 수집 II

### 1. 목표

- Python 기본 문법 실습
- 요청과 응답에 대한 이해
- 데이터 구조에 대한 분석과 이해



### 2. 준비사항

- 사용 데이터
  - TMDB API(https://developers.themoviedb.org/3)
    - 영화 정보 API 서비스
    - 영화 검색 API 서비스
- 개발언어/프로그램
  - Pyrhon 3.8 이상
- 필수 라이브러리
  - `requests`



### 3. 요구사항

커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 데이터를 크롤링 하는 과정을 진행합니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내용 입니다.

- A. 영화 개수 카운트 기능 구현
- B. 특정 조건에 맞는 영화 출력
- C. 평점 순 정렬
- D. 제목 검색, 영화 추천
- E. 배우, 감독 리스트 출력
- F. 추가정보 수집



### 4. 파일/폴더 구조

```
pjt02
     tmdb.py
     README.md
     README.pdf
     problem_a.py
     problem_b.py
     problem_c.py
     problem_d.py
     problem_e.py
     .gitignore
```



## 01. 프로젝트 내용

### 사전 정의 클래스

본 프로젝트를 수월하게 진행하기 위해 `tmdb.py` 에 클래스 및 메서드를 정의하였다.

- TMDB API를 요청할 때 마다, url 설정을 매번 하는 번거로움을 덜고자 한다.

- 필요 정보(key 값, 대분류, 소분류 등)만을 입력하여 원하는 값을 반환받을 수 있다.

```python
import requests	 # 웹에 요청을 보내기 위한 라이브러리


class URLMaker:    
    url = 'https://api.themoviedb.org/3'  # API 요청을 위한 base url

    def __init__(self, key):  # key 값을 받아 인스턴스와 변수 생성
        self.key = key
	
    # API 요청을 위한 url을 생성하는 함수
    def get_url(self, category='movie', feature='popular', **kwargs):
		# url, category, feature, key 값은 요청에 있어 필수 값
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}'
		
        # 편의를 위한 쿼리 설정은 **kwargs로 입력 받아 설정
        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url
        
	# 영화의 고유 id를 요청하여 반환하는 함수
    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        # title(영화 제목)을 입력하여 해당 id를 요청하는 url
        res = requests.get(url)
        movie = res.json()
		
        # dict 형태의 데이터 속에서 id 만을 반환
        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
		# 못 찾았다면 None을 반환
        else:
            return None
```



### A.  영화 개수 카운트 기능 구현

> API를 활용한 클래스를 이용해 데이터로부터 영화 개수를 출력한다.

#### 주요 코드 설명

A 문제는 정상적으로 데이터가 응답하는지에 대한 확인 절차라고 생각한다.

```python
from tmdb import URLMaker  # 사전에 정의한 클래스를 호출
import requests

def popular_count():
    my_key = '7ecf0fa910e1bacb146ddf503cf3ec72'
    url_make = URLMaker(my_key)  # 나의 key 값을 매개변수로 주어, url_make객체 선언
    
    # get_url() 메서드에 영화, 인기, 한국지역, 한국어 등의 쿼리 값을 설정
    url = url_make.get_url('movie','popular',region='KR',language='ko-KR')
	# res를 호출시, 정상이면 200
    res = requests.get(url)
    # json() 메서드로 dict 형변환, popular_list에 할당
    popular_list = res.json()

	# popular_list에는 다음과 같은 dict 데이터가 존재
    '''
    {'page': 1,
     'results': [{'adult': False,
                  'backdrop_path': '/lOSdUkGQmbAl5JQ3QoHqBZUbZhC.jpg',
                  'genre_ids': [53, 28, 878],
                  'id': 775996,
                  'original_language': 'en',
                  'original_title': 'Outside the Wire',
                  'overview': <줄거리 내용>,
                  'popularity': 3533.64,
                  'poster_path': '/e6SK2CAbO3ENy52UTzP3lv32peC.jpg',
                  'release_date': '2021-01-15',
                  'title': '아웃사이드 더 와이어',
                  'video': False,
                  'vote_average': 6.5,
                  'vote_count': 457},
                 {'adult': False,
                  'backdrop_path': '/srYya1ZlI97Au4jUYAktDe3avyA.jpg',
                  'genre_ids': [14, 28, 12],
                  'id': 464052,
                  'original_language': 'en',
                  'original_title': 'Wonder Woman 1984',
                  'overview': <줄거리 내용>,
                  'popularity': 2851.612,
                  'poster_path': '/ss6A2u6YiHTEWeVR01GtTUoO2Xj.jpg',
                  'release_date': '2020-12-23',
                  'title': '원더 우먼 1984',
                  'video': False,
                  'vote_average': 7.1,
                  'vote_count': 3123},
                  {...},
    '''
    
    # 필요한 정보인 '영화들의 개수'를 출력하기 위한 len()
    pop_count = len(popular_list['results'])

    return pop_count
```

#### :bulb: Point

- 저번주에 진행했던 프로젝트의 연장선이다.

  - `.json` 파일이 처음부터 주어지는 것이 아닌, 이번에는 **직접 API를 활용하여 `.json` 을 요청하여 가공**하는 것이다.

- 영화의 개수를 세는 것은 별다른 로직이 필요한 것이 아닌, 

  **사전 정의된 클래스를 이해하고 사용하는지, **

  **선언된 인스턴스의 `get_url()` 메서드가 정상적으로 응답을 하는지**를 테스트하는 과정이라고 생각한다.



### B.  특정 조건에 맞는 영화 출력

> popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화 목록을 출력하 는 기능을 완성한다.

#### 주요 코드 설명

A 문제로부터 파생되어 `dict` 의 구조를 파악하며 **평점 항목**에 접근한다. 

```python
import requests
from tmdb import URLMaker
from pprint import pprint  # dict 형태의 출력값을 정렬하여 보기 편하게 도와주는 라이브러리


def vote_average_movies():
    # 요청 url -> 응답 값 dict로 변환 (위 문제와 동)
    my_key = '7ecf0fa910e1bacb146ddf503cf3ec72'
    url_make = URLMaker(my_key)
    url = url_make.get_url('movie','popular',region='KR',language='ko-KR')
    res = requests.get(url)
    popular_list = res.json()
	
    # 8점이 넘는 영화를 담기위한 리스트
    result_list = []
    
    # 평점 데이터는 ['vote_average']의 value 값
    for movie in popular_list['results']:
        # 평점이 8 이상이라면
        if movie['vote_average'] >= 8:
			# result_list에 해당 영화 데이터를 모두 추가
            result_list.append(movie)

    return result_list
```

#### :bulb: Point

- 저번 주 금요일 프로젝트는 `for loop` 를 3중까지 사용했다. ~~메모리 쌉낭비~~

  - 이번 주 프로젝트는 최대한 `for loop` 사용을 자제하며 코드를 진행하고자 했다.

  

### C. 평점 순 정렬

>  popular를 기준으로 가져온 영화 목록을 평점 순 5개 상위 영화 목록을 출력하는 함수를 완성한다. 

#### 주요 코드 설명

앞선 문제로 인해 평점 항목의 데이터를 가져오기 위해서, 접근 방법은 파악했다.

상위 5개 항목을 출력해야하다보니, **내림차순 정렬**이 가장 효율적일 것으로 와닿았다.

```python
import requests
from tmdb import URLMaker
from pprint import pprint

def ranking():
    # ---- 동일 코드 생략 ----
	res = requests.get(url)
    popular_list = res.json()
    
    # 내장함수 sorted()를 활용 (아래 함수 설명 참고)
    # ['results'] 항목들을 순회하며 정렬할 것인데, 그 중 ['vote_average'] 값을 인자 지정
    # reverse=True로 설정하여 내림차순
    sorted_list = sorted(popular_list['results'], 
                         key=lambda x: x['vote_average'] ,reverse=True)
    
    # 5개를 슬라이싱하면 상위 5개 항목이 출력
    top_5_title = sorted_list[:5]

    return top_5_title
```

- `sorted(iterable[, key=None, reverse=False])`

  - `iterable` : 반복 가능한 객체 (리스트, 문자열, 튜플 등)

  - `key` : 하나의 인자를 받는 함수를 지정

    - 예시

    ```python
    a = [(1, 'c'), (2, 'b'), (3, 'a')]
    
    def position(x):
        return x[1]
    
    print(sorted(a, key=position))
    #=> [(3, 'a'), (2, 'b'), (1, 'c')]
    
    print(sorted(a, key=lambda x: x[1]))
    #=> [(3, 'a'), (2, 'b'), (1, 'c')]
    ```

    - `key` 에 함수를 대입하여 정렬할 인자 대상을 직접 지정해주는 것이다

    - `a` 라는 리스트 안에 3개의 튜플이 있지만,  

      함수 `position()`으로 인해 튜플 중 첫번째 인덱스 자리를 비교하게 되는 것이다.

      `lambda`의 경우도 함수의 기능을 한다. (일회성 함수임 얘는 우선 패스)

  - `reverse` : `True` 로 설정하면 **내림차순**, 기본값인 `Flase`는 **오름차순**

#### :bulb: Point

- `dict` 형태는 `sorted()` 가 안되는 줄 알았다. 이유는 없었다. 그냥 왠지 안될 것 같았다.....
- 모든 값을 `defualt` 로 지정하면 `dict`는 `key` 에 대한 **오름차순** 정렬하는 것을 알 수 있었다.
- 처음에는 로직을 아래와 같이 고민했다...
  - `dict = {'영화 제목': '평점'}` 으로 구성하고... 평점끼리 비교해서.. 해당 영화 제목들을 다시 찾아가서 리스트에서 영화 정보를 호출한다...
  - 너무 비효율적인 것 같아서, 평점 리스트를 만들어서 해당 평점인 영화를 호출하려고 했다.
  - 근데 이러면 평점이 같은 영화는, `for loop` 앞에 걸리는 영화만 주구장창 나올 것이다.
  - 그래서 검색해보니까 `dict` 형태도 `.items(), .values()` 등으로 정렬이 가능한 것을 알았다. :sob: 



### D. 제목 검색, 영화 추천

> 영화제목을 입력하면 그 영화와 관련있는 추천영화 제목 리스트를 반환하는 함수를 완성한다.

#### 주요 코드 설명

TMDB에는 추천영화를 제공하는 API가 존재한다. 

> https://developers.themoviedb.org/3/movies/get-movie-recommendations

경로 설정을 위한 파라미터로 `movie_id` 값을 필요로 한다.

우리는 해당 값을 얻기 위한 메소드를 사전에 정의하였다.

`movie_id()` 메서드에 매개변수로 영화 제목을 입력하면, `movie_id` 값을 반환한다.

새로운 영화추천 API 주소를 위해 반환받은 `movie_id` 값을 `get_url()` 매개 변수로 활용한다.

```python
def recommendation(title):
    my_key = '7ecf0fa910e1bacb146ddf503cf3ec72'
    url_make = URLMaker(my_key)
    # 사용자가 입력한 영화제목에 대한 movie_id 값을 반환
    id_num = url_make.movie_id(title)
    
    # 만약 반환받은 값이 없다면, 똑같이 None을 반환
    if id_num == None:
        return None
	
    # 추천영화 API url을 위한 get_url() 메서드
    # API Doc을 참고하여 자알 설정
    url = url_make.get_url(category='movie', 
                           feature=f'{id_num}/recommendations', language='ko-KR')
    
    res = requests.get(url)
    recmd_list = res.json()
	
    # ['results'] 안의 ['title']로 접근, 제목을 받기 위한 반복문
    titles = [mv['title'] for mv in recmd_list['results']]

    return titles
```

#### :bulb: Point

- 내가 직접 작성한 클래스, 메서드가 아니다보니, 인스턴스 사용에 있어 어버어버 거렸다. :poop:
- 아직 클래스와 메서드는 더 적응이 필요할 것 같다. :cry: :cry: :cry:



### E. 배우, 감독 리스트 출력
> 영화에 출연한 배우들과 감독의 정보가 저장된 딕셔너리를 출력하는 함수를 완성한다.
> 
> cast_id 값이 10보다 작은 배우, department 값이 Directing인 감독
> 
cast, crew 두개의 key를 가지고 각각 배우 리스트와 감독 리스트를 value로 반환

D 과제와 비슷하다.

출연진과 감독진의 정보를 가지고 있는 feature (Credits ) API 또한 `movie_id` 를 필요로 한다!

```python
def credits(title):
    my_key = '7ecf0fa910e1bacb146ddf503cf3ec72'
    url_make = URLMaker(my_key)
    id_num = url_make.movie_id(title)
    
    if id_num == None:
        return None
    # -----------------여기까지는 위와 동일한 코드----------------------

    # Credits API url을 위한 get_url() 메서드
    url = url_make.get_url(category='movie', feature=f'{id_num}/credits', language='ko-KR')
    res = requests.get(url)
    credit_list = res.json()

    # 배우 리스트 / ['cast_id']가 10 이하라면 ['name'] 항목을 리스트에 추가
    cast_list = [info['name'] for info in credit_list['cast'] if info['cast_id'] <= 10]
    
    # 감독 리스트 / ['crew']가 'department'이면 ['name'] 항목을 리스트에 추가
    crew_list = [info['name'] for info in credit_list['crew'] if info['department'] == 'Directing']
    
    # 배우 리스트, 감독 리스트를 value 값으로 한, credits_result(dict 형태) 반환
    credits_result = {'cast': cast_list, 'crew': crew_list}
    
    return credits_result
```

#### :bulb: Point

- 이거 한참 찾았다 진짜로 ㅋㅋㅋ 코드 짜는게 문제가 아니고, 아니 세상 Credits이란 단어를 못찾아서 별군데 다 쑤시고 다녔다.