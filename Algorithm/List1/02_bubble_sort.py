arr = [55, 7, 78, 12, 42]


def bubble_sort(array):  # 정렬할 List
    for i in range(len(array) - 1, 0, -1):  # 범위의 끝 위치
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                # temp = array[j]
                # array[j] = array[j+1]
                # array[j+1] = temp


# j-1, j로 구현해보기

bubble_sort(arr)

print(arr)
