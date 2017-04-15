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

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""

# ============ Lintcode Min&Max Heap ===============
# Time: O(nlogn)
# Space: O(n)
# Trap: int overflow?
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
        
            
# ============= LC ================
# Trap: int overflow?
# Time: add - O(log(n)), find - O(1)
# Space: O(n)
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # Always push to the left heap first, then
        # give the largets to the right_heap to
        # maintain the balance
        heapq.heappush(self.left_heap, num*-1)
        heapq.heappush(self.right_heap, heapq.heappop(self.left_heap)*-1)
        # If two heaps has the same # of emelemts before adding the new
        # one in, the right one will has more after the "shifting", so
        # shift one back.
        if len(self.left_heap) < len(self.right_heap):
            heapq.heappush(self.left_heap, heapq.heappop(self.right_heap)*-1)

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.left_heap and not self.right_heap:
            return None
        
        if len(self.left_heap) == len(self.right_heap):
            return (self.right_heap[0] + self.left_heap[0]*-1)/2.0

        return self.left_heap[0]*-1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
