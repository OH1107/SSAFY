T = int(input())

x=0
result = []
while x < T:
    n = int(input())

    input_list = list(map(int, input().split()))

    for i in range(len(input_list)-1, 0, -1):
        for j in range(0, i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    result.append(input_list)
    x += 1

for idx, _list in enumerate(result):
    print(f'#{idx+1} {" ".join(map(str, _list))}')