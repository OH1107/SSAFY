bit = [0, 0, 0, 0]

# 부분집합의 수는 2^n 개 이다.
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(*bit)
                # 0 0 0 0
                # 0 0 0 1
                # 0 0 1 0
                # ...
                # 1 1 1 1

# 비트 연산을 사용해 부분집합 생성
arr = [3, 6, 7, 1, 5, 4]

n = len(arr) # n : 원소의 개수

for i in range(1<<n): # 1<<n : 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=", ")
    print()
    # 3,
    # 6,
    # 3, 6,
    # ...
    # 3, 6, 7, 1, 5, 4,
