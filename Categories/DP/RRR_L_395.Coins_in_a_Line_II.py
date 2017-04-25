"""
There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? Yes
Example
Given values array A = [1,2,2], return true.

Given A = [1,2,4], return false.
"""

# ============= DP ============
# Time: O(2n)
# Space: O(2n)
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False
            
        lens = len(values)
        if lens <= 2:
            return True
        
        sums = [0]*(lens + 1)
        # build a list of remaining sums
        for i in xrange(1, len(sums)):
            sums[i] = sums[i-1] + values[-i]
        
        dp = [0]*len(sums)
        dp[1] = values[-1]
        for i in xrange(2, len(dp)):
            # don't care who takes first
            # if currently have sums[i] remaining,
            # dp[i] means the most value the current
            # person could take.
            # and dp[i] equals the max among sums[i] - dp[i-1],
            # which is the max value left after the current person 
            # takes the current one and the next person takes
            # the most from the remainings, and sums[i] - dp[i-2],
            # which is if the current person takes two.
            dp[i] = max(sums[i] - dp[i-1], sums[i] - dp[i-2])
        
        return dp[-1] > sums[-1]/2
