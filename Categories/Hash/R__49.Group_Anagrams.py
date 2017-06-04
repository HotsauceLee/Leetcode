"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""

# ============= custom hash key function =============
# Time: O(m*n)
# Sapce: O(n)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
            
        d = {}
        # O(n)
        for s in strs:
            # O(m)
            k = self.gen_key(s)
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
                
        return d.values()
        
    def gen_key(self, s):
        m = [0]*26
        for c in s:
            m[ord(c) - ord('a')] += 1
            
        result = ""
        for idx, val in enumerate(m):
            if val > 0:
                result += chr(idx) + str(val)
                
        return result
