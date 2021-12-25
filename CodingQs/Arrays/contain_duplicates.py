from typing import List
from collections import defaultdict

# Determine if there are multiple copies of a value in the list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False
        
        unique = set(nums)
        unique_nums = list(unique)
        
        return not (len(unique_nums) == len(nums))

# Using dictionary
class Soluition2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        vals = defaultdict(lambda: 0)
        for i in range(len(nums)):
            if vals[nums[i]] == 1:
                return True
            vals[nums[i]] += 1
            
        return False

# Alternative way to use hashmap
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        vals = {}

        for i in nums:
            if i in vals:
                return True
            vals[i] = 1

        return False