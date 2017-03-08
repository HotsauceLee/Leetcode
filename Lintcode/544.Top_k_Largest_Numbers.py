"""
Given an integer array, find the top k largest numbers in it.

Have you met this question in a real interview? Yes
Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].
"""
# ============ Heap =============
# Time: O(nlog(n))
# Space: O(n)
import heapq
class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        
        heap.sort(reverse=True)
        return heap
