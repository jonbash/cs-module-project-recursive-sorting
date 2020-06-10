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


# minor irritation; 'in place' implies no return value, but literally editing
# the array's object in memory, but the tests require a return value -_-
def merge_sort_in_place(arr: list, left=0, right=None):
    right = len(arr) - 1 if right is None else right

    if left >= right:  # already sorted; size <= 1
        return arr

    # merge-sort each half
    mid1 = (left + right) // 2
    mid2 = mid1 + 1
    arr = merge_sort_in_place(arr, left, mid1)
    arr = merge_sort_in_place(arr, mid2, right)

    # merge
    while mid2 <= right:
        if arr[left] > arr[mid2]:
            arr.insert(left, arr.pop(mid2))
            mid2 += 1
        elif left < mid2 - 1:
            left += 1
        else:
            mid2 += 1
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
