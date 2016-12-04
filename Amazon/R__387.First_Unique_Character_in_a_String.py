# ============ List with char as index ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [0]*26
        for c in s:
            d[ord(c) - ord('a')] += 1
        
        i = 0
        while i < len(s):
            c = s[i]
            if d[ord(c) - ord('a')] == 1: return i
            i += 1
        
        return -1
                
