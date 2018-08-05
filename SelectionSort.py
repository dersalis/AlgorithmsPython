from FindSmaller import find_smaller
# Sortowanie przez wybieranie
def selection_sort(arr):
    nArray = []
    for i in range(len(arr)):
        small = find_smaller(arr)
        nArray.append(arr.pop(small))
    return nArray
