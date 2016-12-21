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
# ================== DP ===================
# Timee: O(n)
# Space: O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        max_sub = dp[0]
        
        for i in xrange(1, len(nums)):
            dp[i] = nums[i] + dp[i - 1] if dp[i - 1] > 0 else nums[i]
            max_sub = max(max_sub, dp[i])
            
        return max_sub
