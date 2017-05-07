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

# ================ DP ================
# Time: O(n + n^2 + n^4)
# Space: O(n^3)
class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        if not s1 and not s2:
            return False
        if not s1 or not s2:
            return True
        # pre-check if the two strings have the same chars. O(n)
        if set(s1) != set(s2):
            return False

        lens = len(s1)
        # 3 dimension dp
        # dp[i][j][k] means the if lens k string from i in s1 and j in s2 is scramble to each other
        dp = [[[False]*(lens + 1) for j in xrange(lens)] for i in xrange(lens)]
        # base case fill out single char comparisons.. O(n^2)
        for i in xrange(lens):
            for j in xrange(lens):
                dp[i][j][1] = s1[i] == s2[j]
        
        # iterate each len from 2 to lens, O(n)
        for l in xrange(2, lens + 1):
            # check all len l string, O(n^2)
            for i in xrange(0, lens - l + 1):
                for j in xrange(0, lens - l + 1):
                    # check each partition. O(n!)
                    for k in xrange(1, l):
                        # this partitions the two string from both side
                        regular = dp[i][j][k] and dp[i + k][j + k][l - k]
                        # this is from the opposite side.
                        # s1 first part starts from i and go forward k units.
                        # s2 first part starts from j+l-1-k+1 = j + l - k and go forward k units.
                        # s1 second part starts from i + k and go l - k units.
                        # s2 second part starts from the beginning and go l - k units.
                        opposite = dp[i][j + l - k][k] and dp[i + k][j][l - k]
                        if regular or opposite:
                            dp[i][j][l] = True
                            break
                    
        return dp[0][0][lens]
