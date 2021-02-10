import sys
sys.stdin = open("input.txt", "r")

T = int(input())
x = 0
while x < T:
    n, q = map(int, input().split())
    box_num = []
    hyun_box = [0] * n

    for i in range(1, q+1):
        box_num.append(list(map(int, input().split())))

    for i, LR in enumerate(box_num):
        for j in range(LR[0]-1, LR[1]):
            hyun_box[j] = i+1

    print(f'#{x+1} {" ".join(map(str, hyun_box))}')

    x += 1
