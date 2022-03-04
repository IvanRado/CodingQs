# Insertion sort implementation
def insertionSort(arr: list):

    # Build a sorted sub array starting from the beginning of the list
    # Insert each new element into the correct location
    
    n = len(arr)
    subarr = 1
    for i in range(subarr, n):
        val = arr.pop(i)
        for j in range(subarr):
            print("array", arr)
            print("value", val)
            if val < arr[j]:
                arr.insert(j, val)
                break
        if len(arr) != n:
            arr.insert(subarr, val)
        subarr += 1

    return arr



nums = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertionSort(nums))