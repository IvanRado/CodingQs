from typing import List

# Simple solution; first find difference between entries then calculate 
# the maximum contiguous subarray
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        diffs = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        
        # Find largest combination of differences
        
        curr_sum = diffs[0]
        best_sum = diffs[0]
        
        for j in range(1, len(diffs)):
            curr_sum = max(curr_sum + diffs[j], diffs[j])
            best_sum = max(curr_sum, best_sum)
                    
        if best_sum < 0:
            return 0
        else:
            return best_sum

# Alternative approach
class Solution2:
    def maxProfit(self, prices: List[int]):
        minprice = -999999999
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        
        return maxprofit