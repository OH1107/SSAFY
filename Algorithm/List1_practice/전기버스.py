import sys
sys.stdin = open("input.txt", "r")

T = int(input())
x = 0
while x < T:
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))

    current_position = 0
    goal = True
    charge_count = 0


    while True:
        pass_station = current_position
        current_position += K

        if current_position >= N or (not goal):
            break

        while current_position not in M_list:
            current_position -= 1
            if current_position == pass_station:
                goal = False
                break
        charge_count += 1

    print(f'#{x+1} {charge_count if goal else 0}')

    x += 1