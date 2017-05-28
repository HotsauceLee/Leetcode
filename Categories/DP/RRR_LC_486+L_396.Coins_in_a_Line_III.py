"""
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? Yes
Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.
"""

# ============= DP ============
# Time: O(n + n + n^2)
# Space: O(n + n^2)
# Idea:
"""
max_take[i][j] = max(sum[i][j] - max_take[i + 1][j], sum[i][j] - max_take[i][j - 1]
leave the next person the least.
Build the dp list from smallest section(i == j) to the largest(i = 0, j = len-1)
"""
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 1:
            return True
        
        lens = len(nums)
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
            
        dp = [[0]*lens for i in xrange(lens)]
        for i in xrange(lens):
            dp[i][i] = nums[i]
            
        for l in xrange(2, lens + 1):
            for left in xrange(0, lens - l + 1):
                right = left + l - 1
                cur_sum = sums[right + 1] - sums[left]
                dp[left][right] = max(cur_sum - dp[left + 1][right], cur_sum - dp[left][right - 1])
                
        return dp[0][-1] >= sums[-1]/2.0
