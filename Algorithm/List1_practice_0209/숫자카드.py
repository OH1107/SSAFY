import sys
sys.stdin = open("input.txt", "r")

T = int(input())

x = 0
while x < T:
    N = int(input())
    cards = int(input())

    cnt_list = [0] * 10

    for i in range(N):
        cnt_list[cards % 10] += 1
        cards //= 10

    max_val = cnt_list[0]
    for i in range(len(cnt_list)):
        if max_val <= cnt_list[i]:
            max_val = cnt_list[i]
            max_num = i

    print(f'#{x+1} {max_num} {cnt_list[max_num]}')

    x += 1