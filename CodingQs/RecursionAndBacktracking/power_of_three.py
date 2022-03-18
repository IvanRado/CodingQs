# Given a number n, check if it is a power of 3
# Time complexity: O(n), Space Complexity: O(n)
# Could use memoization if you were to use this operation a lot
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Check if n = 3 or n = 1 (3^0)
        if n/3 == 1 or n == 1:
            return True
        # 
        if n < 3:
            return False
        
        if n % 3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False
        