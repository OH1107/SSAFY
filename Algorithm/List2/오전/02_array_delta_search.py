arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]


# 상하좌우
delta_row = [-1, 1, 0, 0]
delta_col = [0, 0, -1, 1]

# 상하좌우 한번에 할당
delta_row_col = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 추가 - 대각선의 경우는? 좌상, 우상, 우하, 좌하
delta_diagonal = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

# 5(1, 1)의 위치를 기준
r = 1
c = 1

for i in range(4):
    next_row = r + delta_row[i]
    next_col = c + delta_col[i]

    print(arr[next_row][next_col])
    # => 2, 8, 4, 6

# 2(0, 1)의 위치를 기준
r = 0
c = 1
for i in range(4):
    next_row = r + delta_row[i]
    next_col = c + delta_col[i]

    # print(arr[next_row][next_col])
    # => 8, 5, 1, 3
    # 8의 경우 음수 인덱스 또한 파이썬에서는 출력하기 때문
    # 그렇기 때문에 다음과 같이 조건 지정

    N = len(arr) # 행 / 열의 길이
    if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
        continue
    print(arr[next_row][next_col])

    # 혹은
    # if 0 <= next_row < N and 0 <= next_col < N:
    #     print(arr[next_row][next_col])