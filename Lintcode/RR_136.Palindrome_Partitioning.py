# ============ Back tracking + DP palindrome ============
# Time:
# Space:
# NOTICE: DP palindrome is the most important part!!!!!
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if not s or len(s) == 0:
            return []
            
        palindrome_table = self.get_is_palindrome(s)

        def dfs(begin, s, cur_path, result):
            if begin == len(s):
                result.append(cur_path[:])
                return

            for i in xrange(begin, len(s)):
                if not palindrome_table[begin][i]:
                    continue

                cur_path.append(s[begin:i + 1])
                dfs(i + 1, s, cur_path, result)
                cur_path.pop()

        result = []
        dfs(0, s, [], result)
        return result
        
    def get_is_palindrome(self, s):
        str_len = len(s)
        palindrome_table = [[False]*str_len for i in xrange(str_len)]
        
        for single in xrange(str_len):
            palindrome_table[single][single] = True
            
        for pair in xrange(str_len - 1):
            palindrome_table[pair][pair + 1] = s[pair] == s[pair + 1]
            
        for x in xrange(str_len - 3, -1, -1):
            for y in xrange(x + 2, str_len):
                palindrome_table[x][y] = palindrome_table[x + 1][y - 1] and s[x] == s[y]
                
        return palindrome_table
