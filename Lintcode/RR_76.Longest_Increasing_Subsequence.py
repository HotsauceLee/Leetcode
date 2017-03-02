# ============= DP ===============
# Time: O(n^2)
# Space: O(n)
class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
            
        dp = [1]*len(nums)
        max_result = float('-inf')
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_result = max(max_result, dp[i])
                    
        return max(max_result, 1)
