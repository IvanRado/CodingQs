from collections import defaultdict
from itertools import product
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3: return []
        
        # Declare a dictionary - the key will be a value from number and the value will be the number of times it appears
        num_count = defaultdict(int)
        
        # Fill dictionary counts
        for num in nums:
            num_count[num] += 1
                
        result = []
        
        # Edge case of [0,0,0]
        if 0 in num_count and num_count[0] >= 3: 
            result += [[0,0,0]]
        
        # Check if we have the edge case of [a, a, -2a] and verify a != 0
        for a in num_count.keys(): 
            if a != 0 and num_count[a] >= 2 and -2*a in num_count:
                result += [[a, a, -2*a]]
                
        # Get all combinations of positives and negatives (necessary for summing to zero)
        keys = num_count.keys()
        neg = [num for num in keys if num < 0]
        pos = [num for num in keys if num >= 0]
        
        # Check if a c exists that makes the triplet sum to 0
        # Avoid doubling up by having c < a or c > b
        for a, b in product(neg, pos): 
            c = -(a + b)
            if c in num_count and (c < a or c > b):
                result += [[a, b, c]]

        return result