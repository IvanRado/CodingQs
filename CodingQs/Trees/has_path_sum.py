from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# An elegant recursive solution - Time: O(N), Space: O(1)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # No further path
            return False
        
        if targetSum - root.val == 0 and not root.left and not root.right: # Lead node and achieves target
            return True

        targetSum -= root.val        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum) # Recurse on children nodes

# Iterative approach w/ stacks - Space: O(N)
class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        while stack or root:
            while root:
                stack.append(root.val)
                stack.append(root)
                targetSum -= root.val
                root = root.left
            root = stack.pop()
            while type(root) is int:
                targetSum += root
                if not stack: return False
                root = stack.pop()
            if sum == 0 and not root.left and not root.right:
                return True
            root = root.right