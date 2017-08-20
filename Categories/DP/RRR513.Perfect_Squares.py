"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Have you met this question in a real interview? Yes
Example
Given n = 12, return 3 because 12 = 4 + 4 + 4
Given n = 13, return 2 because 13 = 4 + 9
"""
# ============== DP ==============
# Time: O(n)
# Space: O(n)
class Solution:
    # @param {int} n a positive integer
    # @return {int} an integer
    def numSquares(self, n):
        # Write your code here
        if n <= 0:
            return 0
        if n <= 3:
            return n

        dp = [float('inf')]*(n + 1)
        i = 1 
        while i**2 <= n:
            dp[i**2] = 1 
            i += 1

        for i in xrange(1, len(dp)):
            j = 1 
            while j**2 <= i:
                # dp[i - j**2] + 1 = dp[i - j**2] + dp[j**2]
                dp[i] = min(dp[i], dp[i - j**2] + 1)
                j += 1

        return dp[-1]
