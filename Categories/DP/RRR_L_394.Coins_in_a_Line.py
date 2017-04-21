"""
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first play will win or lose?

Have you met this question in a real interview? Yes
Example
n = 1, return true.

n = 2, return true.

n = 3, return false.

n = 4, return true.

n = 5, return true.
"""

# ============= DP ==============
# Time: O(n)
# Space: O(n)
# Idea:
"""
          5
        1/ \2
       4     3
     1/ \2 1/ \2
     3   2 2   1
     
 dp[n] = (dp[n-2] and dp[n-3]) or (dp[n-3] and dp[n-4])
"""
class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n <= 0:
            return False
        if n <= 2:
            return True
        if n == 3:
            return False
        
        
        # dp[n] = (dp[n-2] and dp[n-3]) or (dp[n-3] and dp[n-4])
        dp = [False]*(n+1)
        dp[:4] = [False, True, True, False]
        for i in xrange(4, n+1):
            dp[i] = (dp[i-2] and dp[i-3]) or (dp[i-3] and dp[i-4])
            
        return dp[-1]
