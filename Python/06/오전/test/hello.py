print('hello.py 실행됨')
print(__name__)     # 직접 실행시 '__main__', 호출 됐을 시 모듈 이름

# w직접 파일을 실행했을 때만 실행되는 구문
if __name__ == '__main__':
    print('언제 실행되는걸까?')