arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = 10
for i in range(1 << N):
    SUM = 0
    sub = []
    for j in range(N):
        if i & (1 << j):
            sub.append(arr[j])
            SUM += arr[j]

    if SUM == 10:
        print(sub)

''' =>
[1, 2, 3, 4]
[2, 3, 5]
[1, 4, 5]
[1, 3, 6]
[4, 6]
[1, 2, 7]
[3, 7]
[2, 8]
[1, 9]
[10]
'''