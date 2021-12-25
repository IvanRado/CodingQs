from collections import Counter
from typing import List

# The most straightforward solution using the Counter class
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return counts.most_common(1)[0][0]

# Sort then the majority is at a fixed index: slight worse time complexity but constant space
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# Boyer-Moore voting algorithm; Time: O(n) and Space O(1)
class Solution3:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate