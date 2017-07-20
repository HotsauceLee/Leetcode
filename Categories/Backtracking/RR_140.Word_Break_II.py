"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""

# ================ bt + dp =================
# Time: O(len(s)^2 + ?)
# Space: O(len(s) + ?)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # O(wordDict*word_len)
        words_set = set(wordDict)
        # O(len(s)^2)
        dp = [False]*(len(s) + 1)
        dp[-1] = True
        for outer in xrange(len(s) - 1, -1, -1):
            for inner in xrange(outer, len(s)):
                cur_word = s[outer:inner+1]
                if cur_word in words_set and dp[inner + 1]:
                    dp[outer] = True
                    break
        
        if not dp[0]:
            return []
        
        def dfs(target, start, cur_path, ws, dp, result):
            if start == len(target):
                result.append(cur_path)
                
            for i in xrange(start, len(target)):
                cur_word = target[start:i+1]
                if cur_word in ws and dp[i + 1]:
                    cur_word = ' ' + cur_word if cur_path else cur_word
                    dfs(target, i + 1, cur_path + cur_word, ws, dp, result)
                    
        result = []
        dfs(s, 0, "", words_set, dp, result)
        return result
