"""
Find K-th largest element in N arrays.

 Notice

You can swap elements in the array
"""

# =========== heap ===========
# Time: O(nlog(k))
# Space: O(k)
import heapq
class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        heap = []
        for a in arrays:
            for n in a:
                heapq.heappush(heap, n)
                if len(heap) > k:
                    heapq.heappop(heap)
                    
        
        return heapq.heappop(heap)
