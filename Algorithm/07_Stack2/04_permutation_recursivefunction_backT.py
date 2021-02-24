arr = [1, 2, 3]
n = 3
sel = [0] * n
check = [0] * n

def perm(idx):
    
    # 다 뽑아서 정리했다면
    if idx == n:
        print(sel)
    
    else:
        for i in range(n):
            if check[i] == 0:
                sel[idx] = arr[i]   # 값을 사용해라
                check[i] = 1        # 사용을 했다는 표시
                perm(idx+1)
                check[i] = 0        # 다음 반복문을 위한 원상복구

perm(0)
# =>
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]