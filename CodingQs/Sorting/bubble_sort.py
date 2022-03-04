# Bubble sort implementation
def bubbleSort(arr: list):
    
    # Consider two numbers at a time
    # If the first one is larger, swap them
    # Move to the next two
    # Repeat while swaps have been made

    if len(arr) == 1:
        return arr
    swap = True

    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                tmp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = tmp
                swap = True
    
    return arr


nums = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubbleSort(nums))