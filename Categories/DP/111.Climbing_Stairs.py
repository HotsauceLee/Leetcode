"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Have you met this question in a real interview? Yes
Example
Given an example n=3 , 1+1+1=2+1=1+2=3

return 3
"""
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
