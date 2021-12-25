from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Straightforward recursive solution - Time: O(n), Space: O(1)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        right_depth = self.maxDepth(root.right) + 1
        left_depth = self.maxDepth(root.left) + 1
        
        return max(right_depth, left_depth)

# Iterative solution - Time: O(n), Space: O(n)
class Solution2:
	def maxDepth(self, root):
		max_depth = 0
		stack = [(0, root)]
		while stack:
			level, node = stack.pop()
			if node:
				stack.append((level + 1, node.left))
				stack.append((level + 1, node.right))
			max_depth = max(max_depth, level)
		return max_depth