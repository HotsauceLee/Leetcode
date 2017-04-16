"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

# =========== BS ===========
# Time: O(log(x))
# Space: O(1)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return x
            
        start, end = 1, x
        while start + 1 < end:
            mid = (start + end)/2
            cur_square = mid*mid
            if cur_square == x:
                return mid
            elif cur_square < x:
                start = mid
            else:
                end = mid
                
        if start*start <= x:
            return start
        return end
            
        
