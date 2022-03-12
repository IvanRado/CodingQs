# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.
from typing import List

# Using Kadnes algorithm
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0    

        max_pro , min_pro = nums[0], nums[0]
        
        # Result will store the final max product
        result = max_pro
        
        for i in range(1, len(nums)):
            current = nums[i]
            temp_max = max(current, max_pro*current, current*min_pro)
            min_pro = min(current, max_pro*current, current*min_pro)
            max_pro = temp_max
            result = max(result, max_pro)
    
        return result