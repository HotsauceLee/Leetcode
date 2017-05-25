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
            
# =========== Keep track of last occurance ============
class Solution(object):
    
    """
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret
