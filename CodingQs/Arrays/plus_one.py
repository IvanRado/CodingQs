from typing import List

# Given an array that contains the digits of a large integer, add one to it
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Simple add and return
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            carrying = True
            idx = 1
            while carrying: # While carrying digit
                digits[-idx] = 0
                if idx == len(digits): # First index
                    digits.insert(0, 1) # Insert new digit at start
                    return digits
                else:
                    idx += 1
                    if digits[-idx] == 9: # See if carrying digit continues
                        carrying = True
                    else:
                        digits[-idx] += 1 # Simple add and exit loop
                        carrying = False
                        
            return digits
                    