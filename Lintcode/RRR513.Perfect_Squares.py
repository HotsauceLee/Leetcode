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
                dp[i] = min(dp[i], dp[i - j**2] + 1)
                j += 1

        return dp[-1]
