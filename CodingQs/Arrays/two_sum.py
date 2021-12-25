from typing import List

# Fix one variable, iterate over the rest then move on and repeat
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Corner case
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]
        
        l, r = 0, 1
        while l < len(nums) - 1:
            if nums[l] + nums[r] == target:
                return [l, r]
            
            elif r < len(nums) - 1:
                r += 1
            else:
                l += 1
                r = l + 1