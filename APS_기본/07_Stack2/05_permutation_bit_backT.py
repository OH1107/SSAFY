arr = [1, 2, 3]
n = 3
sel = [0] * n # 뽑은 결과를 출력하기 위함

# check 10진수 정수
def perm(idx, check):
    if idx == n:
        print(sel)
        return

    for i in range(n):
        # i 번째 원소를 활용했군, 그럼 안쓰고 넘어가지
        if check & (1<<i):
            continue
        sel[idx] = arr[i]
        perm(idx+1, check | (1<<i)) # 원상복구가 필요없다...

perm(0,0)
# => 결과는 위와 동