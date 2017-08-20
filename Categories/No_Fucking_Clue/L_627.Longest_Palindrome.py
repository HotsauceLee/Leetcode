"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

 Notice

Assume the length of given string will not exceed 1010.

Have you met this question in a real interview? Yes
Example
Given s = "abccccdd" return 7

One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

# ============== Count # of pairs =============
# Time: O(n)
# Space: O(n)
# Trap: all single ones count as one
class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    def longestPalindrome(self, s):
        # Write your code here
        if not s:
            return 0
        if len(s) <= 1:
            return len(s)
            
        d = set()
        for c in s:
            if c in d:
                d.remove(c)
            else:
                d.add(c)
                
        return len(s) - len(d) + 1 if len(d) > 0 else len(s)
