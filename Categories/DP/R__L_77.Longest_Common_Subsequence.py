"""
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

Have you met this question in a real interview? Yes
Clarification
What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm
Example
For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.

For "ABCD" and "EACB", the LCS is "AC", return 2.
"""

# ================ DP ================
# Time: O(len(A)*len(B))
# Space: O(len(B))
class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0
            
        prev_row = [0]*(len(B) + 1)
        for i in xrange(1, len(A) + 1):
            cur_row = [0]
            for j in xrange(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    cur_row.append(prev_row[j - 1] + 1)
                else:
                    cur_row.append(max(prev_row[j], cur_row[j - 1]))
            prev_row = cur_row
                    
        return cur_row[-1]
