# 5*5 2차 배열에 무작위로 25개의 숫자로 초기화
# 25개의 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절대값을 구하시오
# 25개의 요소에 대해서 모두 조사하여 총합을 구하시오
# 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의

_list = [[1, 4, 5, 9, 3],
        [4, 5, 2, 8, 9],
        [8, 5, 7, 3, 4],
        [9, 4, 1, 6, 3],
        [6, 5, 7, 2, 9]]

d_row = [-1, 1, 0, 0] # 상하
d_col = [0, 0, -1, 1] # 좌우

n = len(_list) # 열의 길이
m = len(_list[0]) # 행의 길이

total_sum = 0
for i in range(n):
    for j in range(m):
        temp_sum = 0
        for k in range(4):
            # i, j에 대한 상하좌우 좌표값
            n_row = i + d_row[k]
            n_col = j + d_col[k]

            # 벽에 있는 요소에 대한 조건
            if n_row < 0 or n_row >= n or n_col < 0 or n_col >= n:
                continue
            
            # 절대값을 구하기 위한 음수, 양수 조건
            if _list[i][j] - _list[n_row][n_col] < 0:
                temp_sum += -(_list[i][j] - _list[n_row][n_col])
            else:
                temp_sum += _list[i][j] - _list[n_row][n_col]
            
        #     print(_list[n_row][n_col], end=" ")
        # print("temp_sum = ", temp_sum)
        total_sum += temp_sum
    # print(total_sum)
print(total_sum)
# print(_list)