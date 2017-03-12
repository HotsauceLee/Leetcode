# =========== Set ============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
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
