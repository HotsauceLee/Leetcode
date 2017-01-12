# =========== DP ============
# Time: O(m*n + m*n)
# Space: O(m*n)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[1]*n for j in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                result[i][j] = result[i-1][j] + result[i][j-1]
                
        return result[-1][-1]
        
# ============ Combination ==========
# Time: O(1)
# Space: O(1)
# Idea: Could move down m - 1 times, move right n - 1 times.
#   Find all the different combinations of those moves.
#   Same as putting picking k items from s set. Picking m - 1 
#   different down moves positions from (m - 1 + n - 1) slots,
#   then the rest are right moves. Same if picking n - 1 first.
from math import factorial
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return factorial(m+n-2)/(factorial(n-1)*factorial(m-1))
