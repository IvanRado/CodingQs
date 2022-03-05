# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# Time Complexity: O(n + m), Space Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # If strings aren't equal length, can't be anagrams
        if len(s) != len(t):
            return False
        
        hash1 = {}
        
        # Put string s into a hashmap
        for char in s:
            if char in hash1.keys():
                hash1[char] += 1
            else:
                hash1[char] = 1
                
        # Go through second string and subtract its letters
        for char in t:
            if char in hash1.keys():
                hash1[char] -= 1
                if hash1[char] < 0:
                    return False
            else:
                return False
            
        for _, value in hash1.items():
            if value != 0:
                return False
            
        return True