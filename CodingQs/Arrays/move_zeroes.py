from typing import List
# Move all zeros to the end of the array while maintaining relative order of other elements
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[idx] = nums[i]
                idx += 1
        
        for j in range(idx, len(nums)):
            nums[j] = 0
        
                