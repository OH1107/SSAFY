arr = [_ for _ in range(1, 11)]     # 전체 집합
l = len(arr)                        # 원소 개수
sel = [0] * l                       # 원소 선택 여부 리스트

res = []

def powerset(idx):
    temp_sum = 0
    temp_list = []
    

    if idx == l:
        for i in range(l):
            if sel[i]:
                temp_sum += arr[i]
                temp_list.append(arr[i])

        if temp_sum == 10:
            print(temp_list)

    else:
        sel[idx] = 0
        powerset(idx + 1)

        sel[idx] = 1
        powerset(idx + 1)

powerset(0)