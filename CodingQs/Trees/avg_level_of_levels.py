from typing import Optional, List
from statistics import mean
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# An iterative solution - Time: O(N), Space: O(m) where m is the width of any given level
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: # Base case
            return []
        
        avg_lvl = []
        queue = [root]
        while queue:
            avg = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                        
                avg.append(node.val)
            avg_lvl.append(mean(avg))
            
        return avg_lvl

# A depth first solution
class Solution2:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        count = []
        res = []
        self.average(root, 0, res, count)
        for i in range(len(res)):
            res[i] = res[i] / count[i]
        return res
    
    def average(self, t: TreeNode, i: int, sums: List[int], count: List[int]):
        if t == None:
            return
        if (i < len(sums)):
            sums[i] += t.val
            count[i] += 1
        else:
            sums.append(t.val)
            count.append(1)
        
        self.average(t.left, i + 1, sums, count)
        self.average(t.right, i + 1, sums, count)        