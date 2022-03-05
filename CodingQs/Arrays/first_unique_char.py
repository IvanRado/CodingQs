# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Time Complexity: O(n), Space Complexity: O(1) -> no more than 26 unique characters
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Base case where s.length == 1 -> return 0
        if len(s) == 1:
            return 0
        
        # Hashmap it
        # key - the letter
        # value - number of times it occurs and earliest index
        letters = {}
        
        for idx in range(len(s)):
            if s[idx] not in letters.keys():
                letters[s[idx]] = [1, idx]
            else:
                letters[s[idx]][0] += 1
                
        print(letters)
        lowest_idx = 10e6 # larger than any possible idx
        
        for key, value in letters.items():
            if value[0] < 2:
                if value[1] < lowest_idx:
                    lowest_idx = value[1]
                
        if lowest_idx == 10e6:
            return -1
        
        return lowest_idx