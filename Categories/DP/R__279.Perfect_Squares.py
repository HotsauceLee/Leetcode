"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

# ============== DP =============
# Time: O(n^2)
# Space: O(n)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return n
            
        dp = [float('inf')]*(n + 1)
        dp[0] = 0
        for i in xrange(1, n + 1):
            j = 1
            while j*j <= i:
                # example:
                # dp[6] = dp[6 - 1 = 5] + 1(1 = 1^2) and dp[6 - 4 = 2] + 1(4 = 2^2)
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
                
        return dp[n]

# =========== Static DP ==============
class Solution(object):
    # only compute the rest on each call
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return n
        if n < len(self._dp):
            return self._dp[n]

        # start from the first one of the rest
        start, end = len(self._dp), n
        # attach the rest
        diff = n - (len(self._dp) - 1)
        self._dp += [float('inf')]*(diff)
        for i in xrange(start, end + 1):
            j = 1
            while j*j <= i:
                self._dp[i] = min(self._dp[i], self._dp[i - j*j] + 1)
                j += 1
                
        return self._dp[n]
        
