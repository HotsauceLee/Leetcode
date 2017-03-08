"""
Find K-th largest element in an array. and N is much larger than k.

 Notice

You can swap elements in the array

Have you met this question in a real interview? Yes
Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.
"""
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
