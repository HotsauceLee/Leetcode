# ============ Backtracking + DP ===============
# Time:
# Space:
class Solution:
    # @param {string} s a string
    # @param {set[str]} wordDict a set of words
    def wordBreak(self, s, wordDict):
        # Write your code here
        def dfs(begin, cur_path, result, s, is_word, dp):
            if not dp[begin]:
                return
            if begin == len(s):
                result.append(' '.join(cur_path))
                return
            
            for i in xrange(begin, len(s)):
                if not is_word[begin][i]:
                    continue
                
                cur_path.append(s[begin: i + 1])
                dfs(i + 1, cur_path, result, s, is_word, dp)
                cur_path.pop()

        is_word = [[False]*len(s) for i in xrange(len(s))]
        for i in xrange(len(s)):
            for j in xrange(i, len(s)):
                is_word[i][j] = s[i:j+1] in wordDict
                
        dp = [False]*(len(s) + 1)
        dp[-1] = True
        for i in xrange(len(s) - 1, -1, -1):
            for j in xrange(i, len(s)):
                if is_word[i][j] and dp[j + 1]:
                    dp[i] = True
                    break
        
        result = []
        dfs(0, [], result, s, is_word, dp)
        return result
