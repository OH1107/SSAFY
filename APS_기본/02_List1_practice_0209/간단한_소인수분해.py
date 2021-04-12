import sys
sys.stdin = open("input.txt", "r")

T = int(input())

i = 0
numbers = []
result = []
while i < T:
    numbers.append(int(input()))
    divisor = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    idx = 0
    while True:
        div_list = [2, 3, 5, 7, 11]

        if numbers[i] % div_list[idx] == 0:
            numbers[i] = numbers[i] // div_list[idx]
            divisor[div_list[idx]] += 1

        elif numbers[i] == 1:
            break

        elif numbers[i] % div_list[idx] != 0:
            idx += 1
    result.append(list(divisor.values()))
    i += 1

for idx, i in enumerate(result):
    count = ' '.join(list(map(str, i)))
    print(f"#{idx + 1} {count}")