"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""

# ================ DP ===================
# Time: O(n^2)
# Space: O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = set(wordDict)
        len_s = len(s)
        dp = [False]*(len_s + 1)
        dp[0] = True
        
        for end in xrange(1, len_s + 1):
            for begin in xrange(1, end + 1):
                dp[end] = dp[end] or (s[begin - 1:end] in d and dp[begin - 1])
                if dp[end]:
                    break
        
        print dp
        return dp[-1]
