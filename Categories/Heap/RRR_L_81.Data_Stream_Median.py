"""
Numbers keep coming, return the median of numbers at every time a new number added.

Have you met this question in a real interview? Yes
Clarification
What's the definition of Median?
- Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].
"""

# ============ Min&Max Heap ===============
# Time: O(nlogn)
# Space: O(n)
import heapq
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums:
            return
        
        cur_median = nums[0]
        left_heap = []
        right_heap = []
        result = [nums[0]]
        
        # O(n)
        for n in nums[1:]:
            if n > cur_median:
                heapq.heappush(right_heap, n)
            else:
                heapq.heappush(left_heap, n*-1)
            # O(log(n))
            if len(right_heap) > len(left_heap) + 1:
                old_median = cur_median
                cur_median = heapq.heappop(right_heap)
                heapq.heappush(left_heap, old_median*-1)
            # O(log(n))
            if len(left_heap) > len(right_heap):
                old_median = cur_median
                cur_median = heapq.heappop(left_heap)*-1
                heapq.heappush(right_heap, old_median)
                    
            result.append(cur_median)
            
        return result
        
            
            
