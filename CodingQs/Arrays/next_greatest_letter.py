import bisect
from typing import List

# Binary Search solution: Time: O(log N), Space: O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        
        l, r = 0, n - 1 # Left and right pointers
        idx = None
        
        while l <= r:
            idx = (l+r)//2 # Mid point
            if letters[idx] > target: # Go down
                r = idx - 1
            elif letters[idx] < target: # Move up
                l = idx + 1
            else:
                break
                
        while idx < n and letters[idx] <= target: # Avoid copies of target in the array
            idx += 1
            
        if idx == n: # Wrap around
            return letters[0]
        else:
            return letters[idx]

# Same thing but with built in functions
class Solution2:
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

# Linear Scan; worse time performance but also a feasible solution
class Solution3:
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]