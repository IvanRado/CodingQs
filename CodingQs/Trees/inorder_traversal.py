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


# Iterative solution
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes_val,track=[],[]
        
        while root!=None:
            
            if root.left!=None:
                track.append(root)  # since Left node should come first, we keep root for next turn
                root=root.left
            elif root.right!=None:   # when left is None but right node exists
                nodes_val.append(root.val)  # we push the root value and traverse the right sub tree
                root=root.right
            else:
                nodes_val.append(root.val)   # when we have reached a leaf node, we push the value and pop from stack
                if len(track)>0:
                    root=track.pop()
                    if root!=None:
                        root.left=None  #  eliminating the left sub tree, since it has already been traversed
                else:
                    root=None  # when track is empty
                    
        return nodes_val