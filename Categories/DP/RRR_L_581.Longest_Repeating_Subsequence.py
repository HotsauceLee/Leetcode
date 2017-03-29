"""
Given a string, find length of the longest repeating subsequence such that the two subsequence don’t have same string character at same position, i.e., any ith character in the two subsequences shouldn’t have the same index in the original string.

Have you met this question in a real interview? Yes
Example
str = abc, return 0, There is no repeating subsequence

str = aab, return 1, The two subsequence are a(first) and a(second). 
Note that b cannot be considered as part of subsequence as it would be at same index in both.

str = aabb, return 2
"""

# ============== DP ==============
# Time: O(n^2) n = len(str)
# Space: O(n^2)
# Idea:
"""
dp[i][j] = max repeating of str[:i + 1] and str[:j + 1]
when str[i] == str[j]:
  dp[i][j] = dp[i-1][j-1] + 1
   e.g. a b a c b c
          i     j
       dp[1][4] = dp[0][3] + 1. dp[0][3] = 1
else:
   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
   e.g. a b a c b c
            i     j
       dp[2][5] = max(dp[1][5], dp[2][4]) = 2
       dp[1][5] = 2, dp[2][4] = 2
"""
class Solution:
    # @param {string} str a string
    # @return {int} the length of the longest repeating subsequence
    def longestRepeatingSubsequence(self, str):
        # Write your code here
        if not str:
            return 0
            
        dp = [[0]*(len(str) + 1) for i in xrange(len(str) + 1)]
        
        for i in xrange(1, len(str) + 1):
            for j in xrange(i, len(str) + 1):
                if i != j and str[i - 1] == str[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        return dp[-1][-1]


# ========== less space ===================
class Solution:
    # @param {string} str a string
    # @return {int} the length of the longest repeating subsequence
    def longestRepeatingSubsequence(self, str):
        # Write your code here
        if not str:
            return 0
            
        prev = [0]*(len(str) + 1)
        cur = [0]*(len(str) + 1)
        
        for i in xrange(1, len(str) + 1):
            for j in xrange(i, len(str) + 1):
                if i != j and str[i - 1] == str[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(cur[j - 1], prev[j])
                    
            prev = cur[:]
                    
        return cur[-1]
