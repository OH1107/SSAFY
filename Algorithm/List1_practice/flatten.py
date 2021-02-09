import sys
sys.stdin = open("input.txt", "r")

x = 0
while x < 10:
    dump = int(input())
    y_box = list(map(int, input().split()))

    for i in range(dump):
        max_value = min_value = y_box[0]
        max_index = min_index = 0

        for j in range(1, len(y_box)):
            if max_value < y_box[j]:
                max_value = y_box[j]
                max_index = j

            if min_value > y_box[j]:
                min_value = y_box[j]
                min_index = j

        y_box[max_index] -= 1
        y_box[min_index] += 1

    max_value = min_value = y_box[0]
    for i in range(1, len(y_box)):
        if max_value < y_box[i]:
            max_value = y_box[i]
        if min_value > y_box[i]:
            min_value = y_box[i]

    print(f'#{x+1} {max_value-min_value}')

    x += 1