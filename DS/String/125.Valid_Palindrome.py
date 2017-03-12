# ========== Two pointers ===========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        begin, end = 0, len(s) - 1
        while begin < end:
            begin_lower = s[begin].lower()
            end_lower = s[end].lower()
            if not begin_lower.isalnum():
                begin += 1
                continue
            if not end_lower.isalnum():
                end -= 1
                continue
            if begin_lower != end_lower:
                return False
                
            begin += 1
            end -= 1
            
        return True
        
        
# ========== another version ===============
class Solution:
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
