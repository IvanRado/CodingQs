from typing import List

# Very straightforward approach, square the array then sort it
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [nums[i]**2 for i in range(len(nums))]
        squared.sort()
        return squared

# A two pointer solution which operates in O(n) time
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]**2]
        
        squared = nums.copy()
        
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        ls, lr = nums[l]**2, nums[r]**2
        while l <= r:
            ls = nums[l]**2
            lr = nums[r]**2
            if lr > ls:
                squared[i] = lr
                r -= 1
                i -= 1
            else:
                squared[i] = ls
                l += 1
                i -= 1
                
        return squared

# Alternative two pointer approach
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:       
        
        i,j = 0, len(nums)-1
        result = []
        while i < j:
            a,b = nums[i] ** 2 , nums[j] ** 2
            if a > b:
                result.insert(0,a)
                i+=1
            else:
                result.insert(0,b)
                j-=1
        result.insert(0, nums[i] ** 2)
        
        return result
