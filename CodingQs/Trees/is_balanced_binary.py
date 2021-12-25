from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive traversal
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Base case
        if root is None:
            return True
        
        hleft=self.findMaxheight(root.left) # Find max height left
        hright=self.findMaxheight(root.right) # Find max height right
        
        if abs(hleft-hright)>1:  # If max heigths differ, definitely unbalanced
            return False
        
        if self.isBalanced(root.left) and self.isBalanced(root.right): # Repeat on children
            return True
        else:
            return False
    
    def findMaxheight(self,root):
        
        if root is None:
            return 0
        
        return max(self.findMaxheight(root.left)+1,self.findMaxheight(root.right)+1) # Return max of two depths