# ============= DP variables =============
# Time: O(n)
# Space: O(1)
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n <= 2:
            return n
            
        prev_prev, prev = 1, 2
        result = None
        for i in xrange(2, n):
            result = prev + prev_prev
            prev_prev = prev
            prev = result
            
        return result
