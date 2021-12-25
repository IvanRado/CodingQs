from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# A nice recursive solution! Time: O(n), Space: O(1)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        
        tmp = root.right
        root.right = root.left
        root.left = tmp
        
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)
        
        return root

# Iterative solution with stacks
class Solution2:
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack.append(node.left)
				stack.append(node.right)

		return root