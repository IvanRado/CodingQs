# Selection sort implementation
def selectionSort(arr: list):
    
    n = len(arr)
    for i in range(n):
        min_elem = float('inf')
        min_index = None
        for j in range(i, n):
            if arr[j] < min_elem:
                min_elem = arr[j]
                min_index = j

        if min_index:
            tmp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = tmp

    return arr


nums = [6, 5, 3, 1, 8, 7, 2, 4]
print(selectionSort(nums))