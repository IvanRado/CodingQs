# Merge sort implementation

def mergeSort(arr: list):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    return merge(
        mergeSort(left),
        mergeSort(right)
    )

def merge(left: list, right: list):
    if len(left) == 1:
        if left[0] > right[0]:
            return right + left
        else:
            return left + right

    l, r = 0, 0
    arr2 = []
    while l < len(left) or r < len(right):
        if l == len(left):
            arr2.append(right[r])
            r += 1
        elif r == len(right):
            arr2.append(left[l])
            l += 1
        else:
            if left[l] < right[r]:
                arr2.append(left[l])
                l += 1
            else:
                arr2.append(right[r])
                r += 1
    
    return arr2

nums = [6, 5, 3, 1, 8, 7, 2, 4]
print(mergeSort(nums))