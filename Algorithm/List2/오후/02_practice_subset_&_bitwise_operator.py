# 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지 탐색

arr=[-2, 1, 9, 3, 4, -3, 5, -6, 8, 2]

n = len(arr) # 원소의 개수
cnt = 0
for i in range(1<<n): # 부분 집합의 개수 (2**n과 동일)
    _sum = 0
    temp = []
    for j in range(n): # 원소의 수만큼 비트를 비교
        if i & (1<<j): # i의 j번재 비트가 1이면 j번재 원소 출력
            temp.append(arr[j])
            _sum += arr[j]
    if _sum == 0:
        cnt += 1
        print(temp)
print(f'합이 0이 되는 조합의 수 : {cnt}')