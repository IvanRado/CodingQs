# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
# Time Complexity: O(n + s) where s is the length of the result as a string
# Space complexity: O(s) 
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        total = 1
        for i in range(2, n+1):
            total *= i
            
        total_str = str(total)
        # print("String of value: " + total_str)
        if total_str[-1] == '0':
            count = 1
          #   print("At least one trailing 0")
            for i in range(2, len(total_str)):
                if total_str[-i] == '0':
                    count += 1
                else: 
                    return count
        else:
            return 0

# Alternative solution that takes advantage of the fact that 0s come after n = 5 
class Solution:
    def trailingZeroes(self, n: int) -> int:
        temp = 0
        
        while n >= 5:
            n = (n//5)
            temp += n
            
        return temp
            