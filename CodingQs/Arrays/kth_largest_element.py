from typing import List

# Trivial solution although the problem is somewhat trivial if you are allowed to sort the list using built in methods

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]