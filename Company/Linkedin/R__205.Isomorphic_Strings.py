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

