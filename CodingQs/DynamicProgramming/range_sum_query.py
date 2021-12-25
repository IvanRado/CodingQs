from typing import List

# Simple solution to a simple problem
class NumArray:
#     create prefix array that calculated sum for every element with their previous elements 
#     result will be right position of the sum - left position of the sum 

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.preSum = [0]* (len(nums)+1)
        for i in range(1,len(nums)+1):
            self.preSum[i]=self.preSum[i-1]+self.nums[i-1]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)