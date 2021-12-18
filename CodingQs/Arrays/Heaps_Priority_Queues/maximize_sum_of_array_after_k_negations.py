from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        # Sort the list
        nums.sort()
        
        # Starting index and length of array
        i = 0
        n = len(nums)
        
        # While the negations remain and we aren't out of bounds
        while (i < n and k > 0):
            
            if nums[i] < 0:  # Negate negative numbers (always an improvement)
                nums[i] *= -1
                k -= 1
                i += 1
                
            elif nums[i] >= 0: # If no negatives remain, break
                break
                
        if k%2==1:  # Negate the smallest number if k is odd
            return sum(nums) - 2*min(nums)
        else:
            return sum(nums) # If k is even, negations can cancel out
                