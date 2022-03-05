# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = s.lower()
        stripped = [char for char in lowercase if char.isalnum()]
        
        l, r = 0, len(stripped) - 1
        while l < r:
            if stripped[l] != stripped[r]:
                return False
            l += 1
            r -= 1
            
        return True