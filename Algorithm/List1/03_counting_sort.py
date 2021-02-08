arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt_list = [0] * (max(arr)+1)
result = [0] * len(arr)

for i in range(0, len(arr)):
   cnt_list[arr[i]] += 1

for i in range(1, len(cnt_list)):
    cnt_list[i] += cnt_list[i-1]

for i in range(len(arr)-1, -1, -1):
    result[cnt_list[arr[i]]-1] = arr[i]
    cnt_list[arr[i]] -= 1

print('array : ', arr)
print('cnt_list : ', cnt_list)
print('result_list : ', result)