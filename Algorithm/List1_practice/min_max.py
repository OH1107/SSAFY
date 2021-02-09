import sys
sys.stdin = open("input.txt", "r")

T = int(input())

x = 0
while x < T:
    N = int(input())
    nums = list(map(int, input().split()))

    min_val = max_val = nums[0]
    for i in range(len(nums)):
        if min_val > nums[i]:
            min_val = nums[i]
        if max_val < nums[i]:
            max_val = nums[i]

    print(f'#{x+1} {max_val - min_val}')

    x += 1