"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

# =============== conditions ==============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
            
        str = str.strip()
        if not str:
            return 0
            
        i, sign = 0, 1
        if str[0] == '+' or str[0] == '-':
            i += 1
            sign = -1 if str[0] == '-' else 1
        
        # print str
        # print ord('0'), ord('9')
        # print sign
        # print i
        result = 0
        while  i < len(str) and ord('0') <= ord(str[i]) <= ord('9'):
            # print ord(str[i])
            result = result*10 + (ord(str[i]) - ord('0'))
            i += 1
        
        result = result*sign
        if result < 0:
            result = max(result, -2147483648)
        else:
            result = min(result, 2147483647)
            
        return result
