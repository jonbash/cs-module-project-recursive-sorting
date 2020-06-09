# no need for helper function
def merge_sort(arr):
    if len(arr) <= 1:  # already sorted
        return arr

    # merge-sort each half
    mid = len(arr) // 2
    arrA = merge_sort(arr[:mid])
    arrB = merge_sort(arr[mid:])

    # merge
    merged = []
    i = j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged.append(arrA[i])
            i += 1
        else:
            merged.append(arrB[j])
            j += 1
    # append any leftover elements if necessary
    if i < len(arrA):
        merged.extend(arrA[i:])
    if j < len(arrB):
        merged.extend(arrB[j:])

    return merged


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
