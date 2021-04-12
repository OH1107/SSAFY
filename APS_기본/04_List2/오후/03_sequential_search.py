# 정렬되어 있지 않은 경우
arr = [4, 9, 11, 23, 19, 7]

def sequentialSearch(_list, key):
    for i in range(len(_list)):
        if key == arr[i]:
            return i
            break
    else:
        return False

print(sequentialSearch(arr, 2))
print(sequentialSearch(arr, 19))


# 정렬되어 있는 경우
arr_2 = [4, 7, 9, 11, 19, 23]

def sequentialSearch2(_list, key):
    for i in range(len(_list)):
        if key == arr_2[i]:
            return i
            break
        elif key < arr_2[i]:
            return f"{i+1}번째 원소까지 검색했지만 없음", False
            break

print(sequentialSearch2(arr_2, 10))
print(sequentialSearch2(arr_2, 9))