"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
"""

# ============= bit ==================
# Time: O(32)
# Space: O(1)
# Idea:
"""
https://discuss.leetcode.com/topic/51999/python-solution-with-no-completely-bit-manipulation-guaranteed

For example, if a is -2 after the loop, a would be 0x00000000FFFFFFFE. What ^mask does here is get a's 32-bit complement, so a^mask = 0x0000000000000001. FYI, this is exactly what ~ in Java would do, -2 in Java is 0xFFFFFFFE, its 32-bit complement is 0x00000001 in Java. Since the output needs to be in 64-bit to be check by OJ, we want 64-bit -2. ~ in Python would convert 0x0000000000000001 to 0xFFFFFFFFFFFFFFFE, which is -2 in Python.

In sum, you can consider a^mask gets a's 32-bit positive complement with more 32-bit 0's on left, and ~ gets the common Python complement.

Basically, this OJ gives us 32-bit integers as input and expects 64-bit integers as output.
"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if not a and not b:
            return 0
        if not a or not b:
            return a or b
        
        MASK, MAX = 0xFFFFFFFF, 0x7FFFFFFF
        while b != 0:
            carry = a&b
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
            
        return a if a <= MAX else ~(a ^ MASK)
