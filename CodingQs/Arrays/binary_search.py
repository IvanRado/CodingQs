from typing import List

# Simple binary search implementation: Time: O(log N), Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        if (n == 1 and nums[0] != target) or not nums:  # Base case, failed to find the target
            return -1
        
        # Iterative solution
        l, r = 0, n-1
        
        while l <= r:
            idx = (l+r)//2
            if nums[idx] > target:
                r = idx-1
            elif nums[idx] < target:
                l = idx + 1
            else:
                return idx
               
        return -1