# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
from typing import List

# Time Complexity: O(n + m), Space Complexity: O(n)
# Use whichever array is smaller to build the hashmap
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        overlap = []
        n1 = {}
        
        # Put first array into hashmap
        for num in nums1:
            if num not in n1.keys():
                n1[num] = 1
            else:
                n1[num] += 1
                
        # Check for existence in hashmap and add to overlap
        for num in nums2:
            if num in n1.keys():
                if n1[num] > 0:
                    overlap.append(num)
                    n1[num] -= 1
        
        return overlap