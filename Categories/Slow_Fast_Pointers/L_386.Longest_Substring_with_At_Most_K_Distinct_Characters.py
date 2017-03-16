"""
Given a string s, find the length of the longest substring T that contains at most k distinct characters.

Have you met this question in a real interview? Yes
Example
For example, Given s = "eceba", k = 3,

T is "eceb" which its length is 4.
"""

#=========== sliding window ============
# Time: O(2n)
# Space: O(n)
class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or k == 0:
            return 0
        if len(s) == 1:
            return 1
            
        slow, d, max_len = 0, {}, float('-inf')
        for fast in xrange(len(s)):
            cur_char = s[fast]
            if cur_char in d:
                d[cur_char] += 1
            else:
                d[cur_char] = 1
                
            while len(d) > k:
                tail_char = s[slow]
                if d[tail_char] > 1:
                    d[tail_char] -= 1
                else:
                    del d[tail_char]
                slow += 1
                    
            max_len = max(max_len, fast - slow + 1)
            
        return max_len
