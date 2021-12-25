from typing import List

# Simple solution using for loop and checking existence in the array
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
    

# Smarter solution using sum of numbers
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = n*(n+1)//2

        for num in nums:
            totalsum -= num
            
        return totalsum