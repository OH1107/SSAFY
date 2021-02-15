# 이진 검색의 시간복잡도는 logn
# 이진 검색은 정렬이 되어있는 상태여야 한다.

def binarySearch(_list, key):
    start = 0
    end = len(_list) - 1

    while start <= end:
        middle = int((start + end) // 2)
        if _list[middle] == key: # 검색 성공
            return f"{middle}번째 인덱스 값"
        elif _list[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False, "검색 실패"

arr = [2, 4, 7, 9, 11, 19, 23]

print(binarySearch(arr, 7))
print(binarySearch(arr, 20))