import sys
sys.stdin = open("input.txt", "r")

T = int(input())
x = 0

while x < T:
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    max_val = min_val = sum(num_list[:m])

    for i in range(n-m+1):
        temp = 0
        for j in range(i, i+m):
           temp += num_list[j]
        if max_val < temp:
            max_val = temp
        elif min_val > temp:
            min_val = temp

    print(f'#{x+1} {max_val - min_val}')

    x += 1