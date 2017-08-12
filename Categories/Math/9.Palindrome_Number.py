"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

Seen this question in a real interview before?   Yes  
"""

# =============== normal compare high and low digit ==================
# Time: ?
# Space: O(1)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x <= 9:
            return True
        
        high, low = 1, 1
        while high <= x:
            high *= 10
        high /= 10
        
        while x:
            high_digit = x/high
            low_digit = x%10
            if high_digit != low_digit:
                return False
            
            x -= high_digit*high
            x /= 10
            high /= 100

            
        return True
