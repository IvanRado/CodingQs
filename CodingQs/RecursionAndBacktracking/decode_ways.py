
# Recursive solution
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        def countWays(i):
            if i == n:
                return 1
            ways = 0
            if 0 < int(s[i]) <= 9:
                ways += countWays(i+1)
            if i < n - 1 and 10 <= int(s[i:i+2]) <= 26:
                ways += countWays(i+2)
            return ways

        return countWays(0)

# DP Solution
class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        prev = 0
        res = 1
        for i in range(n-1, -1, -1):
            t = res
            res = res if 0 < int(s[i]) <= 9 else 0
            res += prev if 10 <= int(s[i:i+2]) <= 26 else 0
            prev = t
        
        return res

# Another DP
class Solution3:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        prevprev = 1
        prev = 0 if s[0] == '0' else 1
        cur = 0
        
        for i in range(2, n+1):
            cur = 0
            if 0 < int(s[i-1:i]) <= 9:
                cur += prev
            if 10 <= int(s[i-2:i]) <= 26:
                cur += prevprev
                
            prevprev, prev = prev, cur
            
        return prev
        
        