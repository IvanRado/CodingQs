from heapq import heappush, heappop
from typing import List

# Find the smallest pairs (sums) between two arrays sorted in ascending order
# Time complexity: O(k * logk), Space complexity: O(k)
class Solution(object):
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(min(len(nums1), k)): # Create the original heap
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        ans = []
        i = j = 0
        while heap:
            _, i, j = heappop(heap)
            smallest_sum = heap[0][0] if heap else float('inf') # Get the first sum
            # Iterate over the indexes of nums2 - we already have the sum of each i and j = 0
            # Append the result while it is less than the smallest sum gotten from the heap
            while j < len(nums2) and nums1[i] + nums2[j] <= smallest_sum:
                ans.append([nums1[i], nums2[j]])
                j += 1
                k -= 1
                if k == 0:
                    return ans
            if j < len(nums2): # Push to heap if we haven't gotten completely through nums2
                heappush(heap, (nums1[i] + nums2[j], i, j))
        return ans