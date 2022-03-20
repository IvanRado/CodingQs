from typing import List

#Time: O(n^2) Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #Every number is a sequence of length 1 on its own
        dp = [1 for _ in range(len(nums))]
        
        #Start by iterating backwards since the last position is always a sequence of length 1
        for idx1 in reversed(range(len(nums) - 1)):
            
            #At each number, iterate forward to check for any increasing subsequence
            for idx2 in range(idx1 + 1, len(nums)):
                if nums[idx1] < nums[idx2]:
                    dp[idx1] = max(dp[idx1], dp[idx2] + 1)
            
        return max(dp)

# Dynamic Programming with Binary Search
# Time: O(nlogn), logn for searching the position for the element's and there are n steps.
# Space: O(n)
from bisect import bisect_left
class Solution2:
	def lengthOfLIS(self, nums):
		dp = []
		for elem in nums:
			idx = bisect_left(dp, elem)
			if idx == len(dp):
				dp.append(elem)
			else:
				dp[idx] = elem
		return len(dp)
    