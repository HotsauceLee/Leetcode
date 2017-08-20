# =========== Dict + set ============
# Time: O(n)
# Space: O(2n)
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) and not len(t):
            return True
            
        d = {}
        pool = set()
        for i in xrange(len(s)):
            if s[i] not in d:
                if t[i] in pool:
                    return False
                d[s[i]] = t[i]
                pool.add(t[i])
            else:
                if d[s[i]] != t[i]:
                    return False
                    
        return True

# ======== Record last appeared position ==========
# Time: O(n)
# Space: O(1)
# Idea:
"""
If s[i] appeared before, check if t[i] appeared in the same position. If ture, update their positions.
If s[i] never appeared before, then check if t[i] appeared before.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) and not len(t):
            return True
            
        d1, d2 = [0]*256, [0]*256
        for i in xrange(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
            
        return True
