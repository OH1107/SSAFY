# 완전 검색 (Brute-force)으로 재귀 순열 생성
def perm(arr, n, k):
    global res

    if k == n:
        if BabyGin(arr, n):
            res = True
        return

    for i in range(k, n):
        arr[k], arr[i] = arr[i], arr[k]
        perm(arr, n, k+1)
        arr[k], arr[i] = arr[i], arr[k]


def BabyGin(tmp, n):

    # 앞 3 숫자 tir, run 검사
    tri_1 = False
    run_1 = False

    if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
        tri_1 = True
    elif tmp[0]+1 == tmp[1] and tmp[1] == tmp[2]+1:
        run_1 = True

    # 뒤 3 숫자 tir, run 검사
    tri_2 = False
    run_2 = False

    if tmp[3] == tmp[4] and tmp[4] == tmp[5]:
        tri_2 = True
    elif tmp[3] + 1 == tmp[4] and tmp[4] == tmp[5] + 1:
        run_2 = True

    if (tri_1 or run_1) and (tri_2 or run_2):
        return True


arr = ['123783', '667767', '054060', '101123']


for i in range(len(arr)):
    res = False
    tmp = list(map(int, arr[i]))
    perm(tmp, len(tmp), 0)
    if res:
        print(f'{tmp} Baby-Gin')

