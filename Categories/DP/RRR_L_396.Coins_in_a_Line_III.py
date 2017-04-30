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
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return 0
        
        lens = len(values)
        # build the sums list. O(n)
        sums = [0]*(lens + 1)
        for i in xrange(1, lens + 1):
            sums[i] = sums[i - 1] + values[i - 1]
        
        # build the dp list. O(n)
        dp = [[0]*lens for i in xrange(lens)]
        for i in xrange(lens):
            dp[i][i] = values[i]

        # sum[i][j] = sums[j] - sums[i - 1]
        # O(n^2)
        for l in xrange(2, lens + 1):
            for i in xrange(0, lens - l + 1):
                j = i + l - 1
                s = sums[j + 1] - sums[i]
                dp[i][j] = max(s - dp[i + 1][j], s - dp[i][j - 1])
                
        return dp[0][-1] > sums[-1]/2
