"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

# ============ Moving window ===========
# Time: O(n)
# Space: O(len(t) + len(s))
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s or len(t) > len(s):
            return ""
        
        pool = {}
        char_count = len(t)
        for c in t:
            if c in pool:
                pool[c] += 1
            else:
                pool[c] = 1

        result = ""
        q = collections.deque()
        for i in xrange(len(s)):
            cur_char = s[i]
            # don't care the chars not in t
            if cur_char not in pool:
                continue
            
            # Put char into the end of q
            q.append((cur_char, i))

            # Plus 1 on the char
            if pool[cur_char] > 0:
                char_count -= 1
            pool[cur_char] -= 1
            
            # Check if has all chars in t
            # if not, continue
            if char_count != 0:
                continue
            
            # if has met all chars, check if we can kick out previous ones
            while pool[q[0][0]] < 0:
                pool[q[0][0]] += 1
                q.popleft()
                
            # update result
            if not result or q[-1][1] - q[0][1] + 1 < len(result):
                result = s[q[0][1]:q[-1][1] + 1]
                
        return result
