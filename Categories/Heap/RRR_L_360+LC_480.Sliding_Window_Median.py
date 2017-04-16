"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
"""

# =========== Bisect maintain sorted window ================
# Time: O(n*(log(k) + k))
# Spce: O(k)
from bisect import insort
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums or k < 1:
            return []
        if k == 1:
            return map(lambda x: x*1.0, nums)

        result, window = [], []
        # O(n)
        for i in xrange(len(nums)):
            # O(log(k))
            insort(window, nums[i])
            if i >= k:
                # O(k)
                window.remove(nums[i-k])
            if i >= k - 1:
                if k%2 == 0:
                    result.append((window[k/2-1] + window[k/2])/2.0)
                else:
                    result.append(window[k/2]*1.0)

        return result

# ============== Min&Max heap TLE ==================
# Time:
# Space: 
import heapq
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of element inside the window at each moving.
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums or k < 1:
            return []
        if k == 1:
            return nums
        
        # True - left has at most 1 more than right
        # False - two heaps must have equal length
        left_size = k/2 if k%2 == 0 else k/2 + 1
        right_size = k - left_size
        left_heap, right_heap, result = [], [], []
        for i in xrange(len(nums)):
            # add the new one in
            # O(log(k))
            heapq.heappush(left_heap, nums[i]*-1)
            # O(log(k))
            heapq.heappush(right_heap, heapq.heappop(left_heap)*-1)
            if len(left_heap) < len(right_heap):
                heapq.heappush(left_heap, heapq.heappop(right_heap)*-1)
            """
            print i
            print "before"
            print left_heap
            print right_heap
            print "\n"
            """
            # delete
            if i >= k:
                delete_target = nums[i - k]
                cur_median = left_heap[0]*-1
                target_heap = right_heap
                if delete_target <= cur_median:
                    target_heap = left_heap
                    delete_target = delete_target*-1
                
                # lazy delete
                popped_out = []
                while target_heap:
                    # O(log(k))
                    cur_popped = heapq.heappop(target_heap)
                    if cur_popped == delete_target:
                        break
                    popped_out.append(cur_popped)
                    
                for po in popped_out:
                    # O(log(k))
                    heapq.heappush(target_heap, po)
                """
                # O(k)
                target_heap.remove(delete_target)
                # O(k)
                heapq.heapify(target_heap)
                """
                # shift from right to left if left doesn't have enough
                # O(log(k))
                if len(left_heap) < left_size:
                    heapq.heappush(left_heap, heapq.heappop(right_heap)*-1)
                if len(right_heap) < right_size:
                    heapq.heappush(right_heap, heapq.heappop(left_heap)*-1)
            """
            print "after"
            print left_heap
            print right_heap
            print "\n"
            """
                
            if i >= k - 1:
                result.append(left_heap[0]*-1)
                
        return result
