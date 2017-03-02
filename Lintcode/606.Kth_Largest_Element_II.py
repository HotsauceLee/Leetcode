# ================ Heap ==================
# Time: O(nlog(n))
# Space: O(n)
import heapq
class Solution:
    # @param nums {int[]} an integer unsorted array
    # @param k {int} an integer from 1 to n
    # @return {int} the kth largest element
    def kthLargestElement2(self, nums, k):
        # Write your code here
        result = []
        for n in nums:
            heapq.heappush(result, n)
            if len(result) > k:
                heapq.heappop(result)
                
        return heapq.heappop(result)
