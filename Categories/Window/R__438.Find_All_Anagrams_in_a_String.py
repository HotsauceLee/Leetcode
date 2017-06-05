"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

# ============== window ==============
# Time:: O(n)
# Space: O(len(p))
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
            
        d = {}
        needed = len(p)
        for c in p:
            d[c] = d[c] + 1 if c in d else 1
        
        result = []
        for idx, val in enumerate(s):
            if val in d:
                d[val] -= 1
                if d[val] >= 0:
                    needed -= 1
                    
            if idx < len(p) - 1:
                continue
            
            if idx > len(p) - 1:
                prev = s[idx - len(p)]
                if prev in d:
                    d[prev] += 1
                    if d[prev] > 0:
                        needed += 1
                    
            if needed == 0:
                result.append(idx - len(p) + 1)
                
        return result
