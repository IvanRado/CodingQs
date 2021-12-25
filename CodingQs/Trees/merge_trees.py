from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursively merge the trees
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: # Moved from a leaf node
            return None
        elif root1 and not root2: # Nothing on the first tree
            return root1
        elif root2 and not root1: # Nothing on the second tree
            return root2
        
        # New root, get the left and right nodes
        root = TreeNode(val=root1.val+root2.val)  
        root.left = self.mergeNodes(root1.left, root2.left)
        root.right = self.mergeNodes(root1.right, root2.right)
        
        return root
        
    def mergeNodes(self, node1: TreeNode, node2: TreeNode):
        
        if not node1 and not node2:
            return None
        elif node1 and not node2:
            return node1
        elif node2 and not node1:
            return node2
        
        node1.val += node2.val
        
        node1.left = self.mergeNodes(node1.left, node2.left)
        node1.right = self.mergeNodes(node1.right, node2.right)
        
        return node1

# Simpler version; avoids code reuse
class Solution2:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # New root, get the left and right nodes
        root = self.mergeNodes(root1, root2)
        
        return root
        
    def mergeNodes(self, node1: TreeNode, node2: TreeNode):
        
        if not node1 and not node2:
            return None
        elif node1 and not node2:
            return node1
        elif node2 and not node1:
            return node2
        
        node1.val += node2.val
        
        node1.left = self.mergeNodes(node1.left, node2.left)
        node1.right = self.mergeNodes(node1.right, node2.right)
        
        return node1

# Single function, slightly slower (?)
class Solution3:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: # Moved from a leaf node
            return None
        elif root1 and not root2: # Nothing on the first tree
            return root1
        elif root2 and not root1: # Nothing on the second tree
            return root2
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

# Also possible to do this iteratively, time complexity a bit longer on average (O(n) vs O(log n))
