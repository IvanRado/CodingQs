# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        curr  = nums[0]
        i = 1
        num_len = len(nums)
        while i < num_len:
            if curr == nums[i]:
                nums.pop(i)
            else: 
                curr = nums[i]
                i += 1
            num_len = len(nums)
                
        return len(nums)