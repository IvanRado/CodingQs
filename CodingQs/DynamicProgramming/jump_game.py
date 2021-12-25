from typing import List


# A relatively simple solution
# First determine if any position can reach the end of the array
# Then trace back to see if we can arrive at that node, repeat until 
# we reach the start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Base cases
        n = len(nums)
        if n == 1: 
            return True
        if nums[0] == 0:
            return False
        
        # Finding max jump from each position and across all positions
        max_reachable = [i + nums[i] for i in range(n-1)]
        max_reach = max(max_reachable)
        
        # No way to reach the end
        if max_reach < (n-1):
            return False
        
        # The last index we need to make it to
        reached = max_reachable.index(max_reach)
        
        # While we haven't evaluated the path
        while reached > 0:
            try:
                max_reach = max(max_reachable[:reached]) # Check the reach from our current spot back
                if max_reach < reached:
                    return False
                reached = max_reachable.index(max_reach) # Find the previous step
            except ValueError:
                reached = -1  # If we can't reach it, set a value to know
            
        if reached == 0: # Found our way back to the start
            return True
        else:  # Failed to find a path
            return False

# More elegant solution that checks similar conditions
# At every point check if the point is reachable and the furthest position it can reach
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        # [3,2,1,0,4]
        #  3,3,3,3,Err
        farthest = 0
        for i in range(len(nums)):
            if i > farthest: # Can't reach current position
                return False
            farthest = max(farthest, i+nums[i])
            if farthest >= len(nums):
                return True
        return True