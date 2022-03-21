# Implement strStr -> Return index of first instance of needle in haystack
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        needle_len = len(needle)
        hay_len = len(haystack)
        
        if needle_len > hay_len:
            return -1
        
        for i in range(hay_len - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i
            
        return -1