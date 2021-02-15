arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

N = 3 # 행의 길이
M = 4 # 열의 길이
# len(arr)
# len(arr[0])

# 행 우선순회 방식
for i in range(N):
    for j in range(M):
        print(arr[i][j])

# 역 행 우선순회 방식
for i in range(N):
    for j in range(M-1, -1, -1):
        print(arr[i][j])

# 열 우선순회 방식
for j in range(M):
    for i in range(N):
        print(arr[i][j])

# 역 열 우선순회 방식
for j in range(M):
    for i in range(N-1, -1, -1):
        print(arr[i][j])

# 지그재그 순회
# 1, 2, 3, 4, 8, 7, 6, 5 ...
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j) * (i%2)])