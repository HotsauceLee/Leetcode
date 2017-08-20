# ============ Recursive ============
# Time: O(log(n))
# Space: O(log(n))
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = -n
            
        return self.myPow(x*x, n/2) if n%2 == 0 else x*self.myPow(x*x, n/2)

# ============ Iterative ==========
# Time: O(log(n))
# Space: O(1)
# Idea:
"""
I couldn't find a clear explanation for an interative Log(n) solution so here's mine. The basic idea is to decompose the exponent into powers of 2, so that you can keep dividing the problem in half. For example, lets say

N = 9 = 2^3 + 2^0 = 1001 in binary. Then:

x^9 = x^(2^3) * x^(2^0)

We can see that every time we encounter a 1 in the binary representation of N, we need to multiply the answer with x^(2^i) where i is the ith bit of the exponent. Thus, we can keep a running total of repeatedly squaring x - (x, x^2, x^4, x^8, etc) and multiply it by the answer when we see a 1.

To handle the case where N=INTEGER_MIN we use a long (64-bit) variable. Below is solution:
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
            
        result = 1
        n_copy = n
        n_copy = abs(n_copy)
        while n_copy:
            if (n_copy&1 == 1):
                result *= x
            n_copy >>= 1
            x *= x
            
        return result if n > 0 else 1/result
