from typing import List

# Super straightforward solution using sets
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = set(range(1, n+1))
        b = set(nums)
        
        return list(a-b)

# Alternative using bit maniupulation - Time: O(n), Space: O(1)
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        val = 0
        for num in nums:
            if val & (1 << num) != 0:
                continue
            val = val ^ (1 << num)
        
        res = []
        for i in range(1, len(nums) + 1):
            if val & (1 << i) == 0:
                res.append(i)
        
        return res