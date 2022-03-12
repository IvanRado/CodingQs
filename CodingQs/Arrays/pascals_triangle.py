# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1,1]] # Starting point
        if numRows == 1: return [[1]]
        if numRows == 2:
            return triangle
        
        for i in range(2, numRows):
            len_row = 1
            row = [1] # Every row starts with a 1
            while j < i:
                row.append(triangle[i-1][len_row] + triangle[i-1][len_row-1]) # Append the sum of the two numbers above it
                len_row += 1 # Increment the length of the row
            row.append(1) # Every row ends with a 1
            
            triangle.append(row)
            
        return triangle
        