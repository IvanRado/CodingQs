from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution - Time: O(N), Space: O(N). Admittedly a bit ugly
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return []
        if not root.left and not root.right:
            return [root.val]
        
        def helper(node: TreeNode):
            if not node:
                return
            
            if not node.left and not node.right:
                return node.val
        
            if node.left:
                ans.append(helper(node.left))
            
            ans.append(node.val)
            
            if node.right:
                ans.append(helper(node.right))
            
        helper(root)
        return [i for i in ans if i != None]

# Recursive solution but cleaner
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def helper(node: TreeNode, path: List[int]):
            if node:
                helper(node.left, path)
                path.append(node.val)
                helper(node.right, path)
                
        
        helper(root, ans)
        return ans