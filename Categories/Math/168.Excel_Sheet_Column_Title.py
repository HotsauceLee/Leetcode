"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
"""

# ================ blah ===============
# Time: ?
# Space: O(1)
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        
        n -= 1
        result = ""
        while n >= 0:
            cur_letter = chr(n%26 + ord('A'))
            result = cur_letter + result
            n = n/26 - 1
        
        return result
