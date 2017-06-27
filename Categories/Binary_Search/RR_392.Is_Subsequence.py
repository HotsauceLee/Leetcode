"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""

# =============== hash + bs ==============
# Time: O(m*log?)
# Space: O(len(t))
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for idx, c in enumerate(t):
            d[c] = [idx] if c not in d else d[c] + [idx]
        
        prev = float('-inf')
        for c in s:
            if c not in d:
                return False
                
            cur_list = d[c]
            cur_list_len = len(cur_list)
            # find the smallest one bigger than prev
            j = self.binary_search(cur_list, prev)
            if j == cur_list_len:
                return False
                
            prev = cur_list[j]

        return True
        
    def binary_search(self, l, t):
        # deal with len 1 list
        if len(l) == 1:
            return 0 if l[0] > t else 1

        begin, end = 0, len(l) - 1
        while begin < end:
            mid = (begin + end)/2
            if l[mid] <= t:
                begin = mid + 1
            else:
                end = mid
                
        return begin
    
    
    
    
