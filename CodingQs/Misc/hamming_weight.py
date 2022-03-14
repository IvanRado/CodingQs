# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight)
# Time Complexity: O(b), Space Complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')