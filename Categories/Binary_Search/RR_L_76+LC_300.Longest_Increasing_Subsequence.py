"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

# ============= DP maintain increasing sequence ============
# Time: O(nlog(n))
# Space: O(n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        len_list = [float('inf')]*(len(nums) + 1)
        len_list[0] = float('-inf')
        
        result = float('-inf')
        for n in nums:
            biggest_smaller = self.__binary_search(len_list, n)
            len_list[biggest_smaller] = n
            result = max(result, biggest_smaller)
            
        return result
        
    def __binary_search(self, l, n):
        left, right = 0, len(l) - 1
        while left < right:
            mid = (left + right)/2
            if l[mid] >= n:
                right = mid
            else:
                left = mid + 1
                
        return left
