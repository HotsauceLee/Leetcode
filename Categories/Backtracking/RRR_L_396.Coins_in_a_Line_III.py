"""
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? Yes
Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.
"""

# ============ Memory Search =============
# Time: O(n^2 + n)
# Space: O(2*n^2)
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False
        
        dp = [[0]*(len(values)) for i in xrange(len(values))]
        max_current = self.__dfs(0, len(values) - 1, values, dp)
        
        return max_current > sum(values)/2
        
    def __dfs(self, left, right, values, dp):
        if left > right:
            return 0
        if dp[left][right] != 0:
            return dp[left][right]

        cur = 0
        if left == right:
            cur = values[left]
        if left == right - 1:
            cur = max(values[left], values[right])
        else:
            l = min(self.__dfs(left + 2, right, values, dp),
                    self.__dfs(left + 1, right - 1, values, dp)) + values[left]
            r = min(self.__dfs(left + 1, right - 1, values, dp),
                    self.__dfs(left, right - 2, values, dp)) + values[right]
            cur = max(l, r)
        
        dp[left][right] = cur
        return cur
