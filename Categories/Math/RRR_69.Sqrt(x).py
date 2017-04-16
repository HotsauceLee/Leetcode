"""
Implement int sqrt(int x).
Compute and return the square root of x.
"""

https://en.wikipedia.org/wiki/Integer_square_root
https://discuss.leetcode.com/topic/24532/3-4-short-lines-integer-newton-every-language
# ========== Integer Newton ===========
# Time: ?
# Space: ?
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return x
            
        r = x
        while r*r > x:
            r = (r + x/r)/2
        return r
