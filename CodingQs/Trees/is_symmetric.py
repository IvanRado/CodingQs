from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Fairly straightforward solution; could simplify by having the inversion and equality checking being in a single function
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root or (root.left == None and root.right == None):
            return True

        left, right = root.left, root.right

        if (left and not right) or (not right and left):
            return False

        right = self.invertTree(right)  # Invert the right subtree
        
        return self.areEqual(left, right) # Recursively check symmetry
        
    def areEqual(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2: # Base case
            return True
        
        if root1 and root2:
            if root1.val == root2.val:
                return self.areEqual(root1.left, root2.left) and self.areEqual(root1.right, root2.right)  # Recurse of children nodes
            else:
                return False # Current nodes are unequal
            
        elif (root1 and not root2) or (not root1 and root2): # Number of nodes differs
            return False
        
        
    # Helper function; the two trees should be equal after inversion
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        
        tmp = root.right
        root.right = root.left
        root.left = tmp
        
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)
        
        return root

# Iterative solution using two stacks and without inverting either subtree
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (root.left == None and root.right == None):
            return True

        left, right = root.left, root.right
        
        if (left and not right) or (not left and right):
            return False
         
        # Check if the two are equal
        stack1 = [left]
        stack2 = [right]
        
        while stack1 and stack2:
            node1, node2 = stack1.pop(), stack2.pop()
            if node1 and node2:
                # print(f"Node 1: {node1}\n Node2: {node2}")
                if node1.val == node2.val:
                    
                    if (node1.left and not node2.right) or (not node1.left and node2.right):
                        return False
                    if (node1.right and not node2.left) or (not node1.right and node2.left):
                        return False
                    
                    stack1.append(node1.left)
                    stack1.append(node1.right)
                    stack2.append(node2.right)
                    stack2.append(node2.left)
                else:
                    return False
            
        
        return True