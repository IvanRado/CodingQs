# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num_col = 0
        for i in range(len(columnTitle)):
            letter_val = ord(columnTitle[i]) - ord('A') + 1
            letter_val *= pow(26, len(columnTitle)-i-1)
            num_col += letter_val
            
        return num_col