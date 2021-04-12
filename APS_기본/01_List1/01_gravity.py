max_cnt = 0
data = list(map(int, input().split()))

for i in range(len(data)):
    cnt = 0
    for j in range(i+1, len(data)):
        if data[i] > data[j]:
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(data)
print(max_cnt)
