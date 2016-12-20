#================ Kadane's algorithm =============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max_so_far = float('-inf')
        for n in nums:
            max_so_far = max(max_so_far + n, n)
            max_sum = max(max_so_far, max_sum)
            
        return max_sum
