"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""

# =============== Sliding window =============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k <= 0:
            return 0

        d = {}
        prev = 0
        result = 0
        for i in xrange(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
                
            while prev < i and len(d) > k:
                if d[s[prev]] > 1:
                    d[s[prev]] -= 1
                else:
                    del d[s[prev]]
                    
                prev += 1
            
            result = max(result, i - prev + 1)
            
        return result
            
