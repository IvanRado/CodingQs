from typing import List


class Solution:
    solutions = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Can select the same one multiple times
        # Need some way to determine unique solutions
        # Each entry is basically its own tree of posibilities to recurse on
        # Know a branch is bad when target < min(candidates)
        
        self.solutions = [] # Need this for multiple test cases 
        
        if target < min(candidates): # Current branch is no good
            return
        
        combs = []
        for cand in candidates:
            path = []
            path.append(cand)
            combs.append(self.paths(candidates, target-cand, path))
        
        return self.solutions
        
    def paths(self, candidates: List[int], target: int, curr: List[int]) -> List[List[int]]:
        if target == 0: # Exit condition
            curr.sort() # Sort for uniqueness
            if curr not in self.solutions: # Avoid duplicates
                self.solutions.append(curr)
            return curr
        
        if target < min(candidates): # No solution along this branch
            return []
        combs = []
        for cand in candidates:
            path = curr.copy()
            path.append(cand)
            combs.append(self.paths(candidates, target-cand, path))
        
        return combs


# Cleaner recursion; avoids some bad branches by preventing us from going back in indexes as we go along
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def recurse(ans, current_sum, current_combination, index):
            if current_sum > target:
                return
            elif current_sum == target:
                ans.append(current_combination)
            else:
                for i, candidate in enumerate(candidates[index:]):   
                    recurse(ans, current_sum + candidate, current_combination + [candidate], index + i)
        recurse(ans, 0, [], 0)
        return ans