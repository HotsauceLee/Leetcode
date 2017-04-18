"""
Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.
Indices of the integers in the subsequence should be continuous.
 Notice

O(n) time and O(1) extra space.

Have you met this question in a real interview? Yes
Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.
"""

# ============= DP =============
# Time: O(n)
# Space: O(1)
class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if not A:
            return 0
            
        max_increase = max_decrease = 1
        cur_increase = cur_decrease = 1
        for i in xrange(1, len(A)):
            if A[i] > A[i-1]:
                cur_increase += 1
                cur_decrease = 1
            elif A[i] < A[i-1]:
                cur_decrease += 1
                cur_increase = 1
            else:
                cur_increase += 1
                cur_decrease += 1
            
            max_increase = max(max_increase, cur_increase)
            max_decrease = max(max_decrease, cur_decrease)

        return max(max_increase, max_decrease)
