from typing import List

# One possible solution that uses prefix and suffix arrays
# Scan the array - prefix is the product of all values before i, suffix is the same for values after i
# Multiply the values of the prefix and suffix to get the solution
# Time: O(N), Space: O(N); technically both are 2N
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_pre = 1
        sum_post = 1
        soln = []
        prefix, suffix  = [1], [1]
        
        
        for i in range(1, n):
            sum_pre *= nums[i-1]
            sum_post *= nums[-i]
            prefix.append(sum_pre)
            suffix.insert(0, sum_post)
            
        for i in range(n):
            soln.append(prefix[i]*suffix[i])
            
        
        return soln

# Space O(1) solution
# We take a similar approach, except this time we construct the output array/solution in place
# Additionally only requires a single pass of the array!
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Array length, zero count, prefix and suffix sums
        n = len(nums)
        sum_pre, sum_post = 1, 1 
        soln = [1, 1]
        zeroes = 0
        
        # Increment zeroes and switch over indexes
        if nums[0] == 0: zeroes += 1
        pre, post = n//2, n//2
        
        # In the first half we are inserting elements into the solution array
        for i in range(1, pre):
            if nums[i-1] == 0 or nums[-i] ==0:
                zeroes += 1
            sum_pre *= nums[i-1]
            sum_post *= nums[-i]
            soln.insert(i, sum_pre)
            soln.insert(-i, sum_post)
            
        if n % 2 == 1: # If the array has an odd number of elements, we insert it here
            sum_pre *= nums[n//2 - 1]
            sum_post *= nums[n//2 + 1]
            soln.insert(pre, sum_pre*sum_post)
            post += 1
            
        for i in range(post, n): # In the second half we multiply the existing array values with the prefix and suffix products
            sum_pre *= nums[i-1]
            sum_post *= nums[-i]
            soln[i] *= sum_pre
            soln[n-1-i] *= sum_post
            
        # If there is more than one zero, the entire array is zeroes 
        if zeroes >= 2:
            return [0]*n     
        
        return soln