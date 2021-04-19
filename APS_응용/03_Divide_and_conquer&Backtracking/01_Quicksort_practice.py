def qsort(a, low, high):
    if low < high:
        pivot = partition(a,low,high)
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high)

def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j


tc_1 = [11, 45, 23, 81, 28, 34]
tc_2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
tc_3 = [1, 1, 1, 1, 1, 0, 0, 0, 0]

qsort(tc_1, 0, len(tc_1)-1)
print(tc_1)
# => [11, 23, 28, 34, 45, 81]

qsort(tc_2, 0, len(tc_2)-1)
print(tc_2)
# => [8, 11, 17, 22, 22, 23, 34, 45, 81, 99]

qsort(tc_3, 0, len(tc_3)-1)
print(tc_3)
# => [0, 0, 0, 0, 1, 1, 1, 1, 1]