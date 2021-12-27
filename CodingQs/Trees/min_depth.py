from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution - Time: O(N), Space: O(1)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # Null node
            return 0
        
        if not root.left and not root.right: # Leaf node condition
            return 1
            
        if root.left and root.right: # Min if both branches exist
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left and not root.right: # Left branch
            return self.minDepth(root.left, 1)
        else: # Right branch
            return self.minDepth(root.right, 1)
        
# Iterative solution
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = [root] # FIFO Queue
        depth = 0
        while queue: # While more levels are to be explored
            depth = depth + 1
            for _ in range(len(queue)): # Iterate over current level
                node=queue.pop(0) # Pop the top element
                if node.left == None and node.right == None:
                    return depth # Exit if leaf
                elif node.left:
                    queue.append(node.left) # Append left
                if node.right:
                    queue.append(node.right) # Append right
        return -1