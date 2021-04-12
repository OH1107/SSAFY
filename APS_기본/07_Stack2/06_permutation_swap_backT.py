arr = [1, 2, 3]

n = 3

def perm(idx):
    if idx == n:
        print(arr)

    else:
        for i in range(idx, n):
            # 순서를 바꾸고
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx + 1)
            
            # 원상복구
            arr[idx], arr[i] = arr[i], arr[idx]

perm(0)