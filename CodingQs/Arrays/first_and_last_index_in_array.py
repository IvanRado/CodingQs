from typing import List

# Find the first and last index of a target value in a given array (sorted in non-descending order)
# Complexity Analysis - Time: O(log N) - A binary search + some constant time to find the full width; worst case is O(n) though
# Space: O(1) - only three pointers are used at any time
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
            
        idx = self.binarySearch(nums, target)
        if idx == -1:
            return [-1,-1]
        
        left = right = idx
        while left >= 0 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1
        
        return [left+1, right-1]
            
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)
        idx = (right+left)//2
        
        while left < right:
            idx = (right+left)//2
            val = nums[idx]
            if val < target:
                left = idx+1
            elif val > target:
                right = idx
            else:
                return idx
            
        return -1

# A recursive solution
class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findEdge(step):
            L = len(nums)
            l, r = 0, L-1
            
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if (step == 1 and mid == L-1) or nums[mid + step] != target:
                        return mid
                    elif (step == -1 and mid == 0) or nums[mid + step] != target:
                        return mid
                    
                    if step == 1:
                        l = mid+1
                    else:
                        r = mid-1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            
            return -1
                    
        
        return [findEdge(-1), findEdge(1)]  
                