from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterate through the root tree and check if each node is a subtree
# Time: O(n*m), Space: O(n)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:  
            return True
        
        stack = [root] # Start at the root node
        same = False
        while stack: # While haven't checked all nodes
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                same = self.isSame(node, subRoot)
                if same: # Return is subtree found
                    return True
                
        return same
               
    def isSame(self, r1: TreeNode, r2: TreeNode) -> bool:
        if not r1 and not r2:
            return True
        if r1 and r2:
            if r1.val == r2.val:
                return self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)
            else: 
                return False
        return False

# Alternative approach that uses O(1) memory
class Solution2:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False     
        
        return  self.check_if_subtree(root, subRoot) or \
                self.isSubtree(root.right, subRoot) or \
                self.isSubtree(root.left, subRoot)
        
    # Checks if two nodes have the same structure  
    def check_if_subtree(self, root1: TreeNode, root2:TreeNode):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False
        return self.check_if_subtree(root1.right, root2.right) and self.check_if_subtree(root1.left, root2.left)