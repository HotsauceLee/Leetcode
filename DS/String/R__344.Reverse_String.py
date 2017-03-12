# ======== Pointers ==============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        l = 0
        r = len(s_list) - 1
        while l < r:
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
            
        return ''.join(s_list)
    
    """
    cheating:
    
    return s[::-1]
    return ''.join(reversed(s))
    """
    
    """
    def reverseString(self, s):
        if len(s)<=1:
            return s
        n=len(s)
        return self.reverseString(s[n//2:])+self.reverseString(s[:n//2])
    """
