# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Time Complexity: O(n*log(n)), Space Complexity: O(n) (or O(1) if return array is not considered)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals such that those with the lowest start point are at the front
        # Declare start of interval
        # Check if end of interval overlaps with start of next
        # If it does, merge them
        # If it doesn't, push the old one
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        start = intervals[0][0] # Start of the first interval
        end = intervals[0][1]
        
        for i in range(1, len(intervals)): 
            interval = intervals[i]
            if end >= interval[0]:
                end = max(end, interval[1]) 
                start = min(start, interval[0]) 
            else:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
        
        merged.append([start, end])
        
        return merged