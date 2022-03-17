# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        vals = {}
        new_val = True
        digits = [int(c) for c in str(n)]
        
        while new_val:
            print(digits)
            sum_of_digits = 0
            for digit in digits:
                sum_of_digits += digit**2
                
            if sum_of_digits == 1:
                return True
            
            if sum_of_digits in vals.keys():
                return False
            else:
                vals[sum_of_digits] = 1
                
            digits = [int(c) for c in str(sum_of_digits)]
                
        return False