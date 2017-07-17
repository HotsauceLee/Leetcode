"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
Seen this question in a real interview before?   Yes  
"""

# ============= mask ================
# Time: O(32)
# Space: O(1)
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = ~0
        while mask&num:
            mask <<= 1
            
        return ~mask & ~num
        
     
# ============= first 0 bit =============
# Time: O(32)
# Space: O(1)
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        first_zero = 1
        while first_zero <= num:
            first_zero <<= 1
            
        return (first_zero - 1)^num
