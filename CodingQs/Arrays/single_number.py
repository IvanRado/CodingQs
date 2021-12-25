from typing import List
from functools import reduce

# Bit-wise solution using XOR; Time - O(n), Space - O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor

# Single line solution that uses the same idea
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)