# 반복
def selectionSort(_list, n):
    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            if _list[min_index] > _list[j]:
                min_index = j

        _list[i], _list[min_index] = _list[min_index], _list[i]
    return


# 재귀
def RecursionSelectionSort(_list, n, k):
    if k == n:
        return

    min_index = k
    for i in range(k+1, n):
        if _list[min_index] > _list[i]:
            min_index = i

    _list[k], _list[min_index] = _list[min_index], _list[k]

    RecursionSelectionSort(_list, n, k+1)


arr = [3, 6, 2, 1, 8, 5, 4, 9, 7]
arr_2 = [3, 6, 2, 1, 8, 5, 4, 9, 7]

selectionSort(arr, len(arr))
print(arr) # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

RecursionSelectionSort(arr_2, len(arr_2), 0)
print(arr_2) # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]



