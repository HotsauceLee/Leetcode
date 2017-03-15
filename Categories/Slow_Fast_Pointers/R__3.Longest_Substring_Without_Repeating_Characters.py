"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# =========== slow fast pointers + hashset ===========
# Time: O(2n)
# Space: O(n)
# Trap: how to keep the set non-repeat
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
            
        slow, longest = 0, float('-inf')
        d = set()
        for fast in xrange(len(s)):
            cur_char = s[fast]
            if cur_char not in d:
                longest = max(longest, fast - slow + 1)
                d.add(cur_char)
            else:
                while s[slow] != cur_char:
                    d.remove(s[slow])
                    slow += 1
                slow += 1
                
        return longest
