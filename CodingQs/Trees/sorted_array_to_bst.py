from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Elegant recursive solution, Time: O(n), Space: O(n)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # Middle index will be the value of root
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(val=nums[0])
        
        
        root = TreeNode(nums[n//2])
        left_vals, right_vals = nums[:n//2], nums[n//2+1:]
        root.left = self.sortedArrayToBST(left_vals)
        root.right = self.sortedArrayToBST(right_vals)
        
            
        return root
        
        