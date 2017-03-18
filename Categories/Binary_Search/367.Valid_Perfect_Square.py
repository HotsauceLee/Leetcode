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

# ============ Binary Search ============
# Time: O(log(n))
# Space: O(1)
# Trap: mid overflow, not a python problem, but use long in JAVA
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
            
        left, right = 1, num
        while left < right:
            mid = (left + right)/2
            mid_square = mid**2
            if mid_square == num:
                return True
            if mid_square > num:
                right = mid
            else:
                left = mid + 1
                
        return False
