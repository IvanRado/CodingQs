# Given a roman numeral, convert it to an integer

# Time Complexity: O(n), Space Complexity: O(C) where C is the number of unique roman numeral combinations
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {  # Dictionary of potential values
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        if len(s) == 1: # Base case
            return values[s]
        
        # 
        total = 0
        double = False
        i = 0
        while i < len(s): # Scan the string
            snip = s[i:i+2] # Check for potential two letter combinations
            if snip in values.keys(): # If it's a two letter combination, add the modified version and jump two
                total += values[snip]
                double = True
                i += 2
            else: # Otherwise add the first numeral and move forward
                total += values[snip[0]]
                double = False
                i += 1
        
        # If we finished on a double return
        if double:
            return total
        else: # Otherwise add the final value as well
            return total + values[s[-1]]
            