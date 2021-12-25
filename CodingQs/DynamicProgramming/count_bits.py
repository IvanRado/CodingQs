from typing import List

# Simple solution using iterations over the string representation of the ints
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        results = []
        for i in range(n + 1):
            bin_str = bin(i)[2:]
            result = 0
            for i in range(len(bin_str)):
                if bin_str[i] == '1':
                    result += 1
                
            results.append(result)
                
        return results

# Dynamic programming solution
# Makes use of the fact that even numbers are their halves shifted left by one with added 0
# And odds are their halves shifted left by one with added 1
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ## base case
        # 0 = 0b 0
        dp = [0]
        
        ## general cases
        for i in range(1, n+1):
            
            if i & 1 == 0:
                # even number = (n//2) << 1, with adding 0 on the LSB
                dp.append( dp[ i//2] )
            
            else:
                # odd number = (n//2) << 1 + 1 = (n//2) << 1 | 1, with adding 1 on the LSB
                dp.append( dp[ i//2] + 1 )
                
        return dp