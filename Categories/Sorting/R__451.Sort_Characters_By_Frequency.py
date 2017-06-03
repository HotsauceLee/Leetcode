"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

# ================ store every char/one char in result =============
# time: O(n + nlog(n) + n)
# Space: O(n)
class Node(object):
    def __init__(self, ch, count, first_index):
        self.ch = ch
        self.count = count
        self.i = first_index

    def __cmp__(self, other):
        if self.count != other.count:
            return other.count - self.count
        return self.i - other.i
        
    def __str__(self):
        return self.ch*self.count # delete *self.count if only want one char in result

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        d = {}
        for idx, c in enumerate(s):
            if c in d:
                d[c].count += 1
            else:
                d[c] = Node(c, 1, idx)
                
        char_list = sorted(d.values())
        result = ''
        for n in char_list:
            result += str(n)
        return result

# ============= use count map ============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        d = [0]*256
        max_count = 0
        # O(n)
        for c in s:
            d[ord(c)] += 1
            max_count = max(max_count, d[ord(c)])
        
        conut_map = [None]*(max_count + 1)
        # O(n)
        for c in s:
            count = d[ord(c)]
            if count == 0:
                continue

            if not conut_map[count]:
                conut_map[count] = [c]
            else:
                conut_map[count].append(c)
                
            d[ord(c)] = 0
        
        result = ""
        # O(n)
        for i in xrange(len(conut_map) -1 , -1, -1):
            if not conut_map[i]:
                continue
            
            for cm in conut_map[i]:
                result += cm*i
                
        return result
