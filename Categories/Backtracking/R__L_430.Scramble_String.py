"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Have you met this question in a real interview? Yes

"""

# ============== Memorized Backtracking =============
# Time: ?
# Space: ?
class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    d = {}
    def isScramble(self, s1, s2):
        # Write your code here
        if not s1 and not s2:
            return True
        if not s1 or not s2:
            return False
        len1, len2 = len(s1), len(s2)
        if len1 != len2:
            return False
        if len1 == 1:
            return s1 == s2
        if s1 + '#' + s2 in self.d:
            return self.d[s1 + '#' + s2]
            
        left, right = 0, len1 - 1
        for i in xrange(left, right):
            # s2 partition to s2[:i + 1] and s2[i + 1:]
            # but check same partition of s1 from both head and tail
            s1_from_head = self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:])
            s1_from_tail = self.isScramble(s1[-1 - i:], s2[:i + 1]) and self.isScramble(s1[:-1 - i], s2[i + 1:])
            if s1_from_head or s1_from_tail:
                self.d[s1 + '#' + s2] = True
                return True

        self.d[s1 + '#' + s2] = False
        return False
