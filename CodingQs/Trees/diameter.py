import math
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS solution w/recursion; could also use nonlocal instead of a new class param
class Solution:
    dia=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root==None:
                return -1
            ls=height(root.left)
            rs=height(root.right)
            self.dia=max(self.dia,ls+rs+2) 
            return max(ls,rs)+1
			
        height(root)
        return self.dia