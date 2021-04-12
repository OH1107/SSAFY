arr = [10, 15, 2, 19, 6, 14]

def selectionSort(_list):
    for i in range(len(_list)-1):
        min_index = i

        for j in range(i+1, len(_list)):
            if _list[min_index] > _list[j]:
                min_index = j

        _list[i], _list[min_index] = _list[min_index], _list[i]
    return _list

print(selectionSort(arr))
