from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Find the maximum contiguous subarray and return the sum
        curr_sum = nums[0]
        best_sum = nums[0]
        
        for i in range(len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            best_sum = max(best_sum, curr_sum)
            
        return best_sum
        
        