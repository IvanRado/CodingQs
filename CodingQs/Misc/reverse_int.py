# Given an integer, return the integer with the digits reversed
# If it falls outside the range of a signed 32-bit integer, return 0
# Time Complexity: O(d), Space Complexity: O(d)
class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        
        
        end = 0 if string[0] != "-" else 1
        new_str = "-" if string[0] == "-" else ""
        for i in range(len(string)-1, end - 1, -1):
            new_str += string[i]
        
        
        print(new_str)
        rev = int(new_str)
        return rev if -2**31 <= rev <= 2**31 - 1 else 0