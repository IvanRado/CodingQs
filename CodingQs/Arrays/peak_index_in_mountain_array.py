from typing import List

# Trivial solution - Time: O(N), Space: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 3: # Base case
            return 1
        return arr.index(max(arr))

# Binary Search - Time: O(log N), Space: O(1)
class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 3: # Base case
            return 1
        
        l, r = 0, n-1
        
        while l <= r:
            idx = (l+r)//2
            if (arr[idx-1] < arr[idx]) and (arr[idx] > arr[idx+1]): # Bigger than neighbors -> mountain
                return idx
            elif arr[idx+1] > arr[idx]: # climbing up
                l = idx+1
            elif arr[idx-1] > arr[idx]: # Coming down
                r = idx-1
               
        return idx    
        