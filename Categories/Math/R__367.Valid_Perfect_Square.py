"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.
"""

# ============= 1+3+5+7+.....===========
# Time: O(sqrt(n))
# Space: O(1)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num or num < 0:
            return False
        if num <= 1:
            return True
            
        base = 1
        while num > 0:
            num -= base
            base += 2
                
        return num == 0
