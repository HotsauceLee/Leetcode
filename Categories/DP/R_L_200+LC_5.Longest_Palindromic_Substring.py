"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

# =============== DP ===================
# Time: O(n^2)
# Space: O(n^2)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        dp = [[False]*len(s) for i in xrange(len(s))]
        
        result = ""
        for j in xrange(len(s)):
            for i in xrange(0, j + 1):
                if i == j:
                    dp[i][j] = True
                elif i == j - 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                    
                if dp[i][j]:
                    if j - i + 1 > len(result):
                        result = s[i:j+1]
                        
        return result
        
