# This solution is elegant but exceeds the time limit :(

class Solution:
    def climbStairs(self, n: int) -> int:
        # step n = a * step_size_1 + b*step_size_2
        # With each step we add a number of possibilities equal to the previous two
        # Kinda like a Fibonacci sequence
        def combinations(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 3
            
            return combinations(n-1) + combinations(n-2)
        
        return combinations(n)

# Same idea as above but with memoization
class Solution2:
    def climbStairs(self, n: int) -> int:
        def combinations(n: int, computed: dict = {1: 1, 2: 2, 3:3}) -> int:
            if n not in computed:
                computed[n] = combinations(n-1, computed) + combinations(n-2, computed)
            return computed[n]
            
        return combinations(n)

# Faster solution w/out recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1): return 1
        if(n == 2): return 2
        
        thisOne = 1
        nextOne = 2
        temp = 0
        for i in range(2, n, 1):
            temp = thisOne + nextOne
            thisOne = nextOne
            nextOne = temp
        
        return nextOne