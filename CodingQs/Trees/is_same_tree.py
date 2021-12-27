from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Simple recursive solution - Time: O(N), Space: O(1)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # Base case
            return True
        
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
            
        return False

# Iterative solution using two stacks - Time: O(N), Space: O(N)
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        stack1 = [p]
        stack2 = [q]
        
        while stack1 and stack2:
            node1, node2 = stack1.pop(), stack2.pop()
            if node1 and node2:
                if node1.val == node2.val:
                    stack1.append(node1.left)
                    stack1.append(node1.right)
                    stack2.append(node2.left)
                    stack2.append(node2.right)

                else:
                    return False
            
            elif (node1 and not node2) or (not node1 and node2):
                return False

        return True
