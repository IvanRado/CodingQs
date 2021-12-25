from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Traverse the tree, adding the value of a given node if it falls between low and high 
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
    
        self.low = low
        self.high = high
        
        if root.val >= low and root.val <= high:
            value_sums = root.val
        else:
            value_sums = 0
            
        return self.sum_branch(root.left, 0) + self.sum_branch(root.right, 0) + value_sums
            
        
    def sum_branch(self, node: TreeNode, sums: int):
        if not node:
            return sums
        
        if node.val >= self.low and node.val <= self.high:
            sums += node.val
            
        return self.sum_branch(node.left, 0) + self.sum_branch(node.right, 0) + sums
        

# Cleaner depth first solution
class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        res = root.val if low <= root.val <= high else 0
        if root.val <= low: return res + self.rangeSumBST(root.right, low, high) # Only the right branch is in range
        if root.val >= high: return res + self.rangeSumBST(root.left, low, high) # Only the left branch is in range
        return res + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high) # Need sum of both branches
        