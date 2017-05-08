"""
Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the coordinate of the left-up and right-down number.

Have you met this question in a real interview? Yes
Example
Given matrix

[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
return [(1,1), (2,2)]
"""

# ============ prefix sum ==============
# Time: o((mn)^2)
# Space: O(mn)
class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        if not matrix or not matrix[0]:
            return []
        
        len_row, len_col = len(matrix), len(matrix[0])
        # dp[i][j] is the sum from (0, 0) to (i-1, j-1)
        # O(m*n)
        dp = [[0]*(len_col + 1) for i in xrange(len_row + 1)]
        # build the sum(dp) array. O(m*n)
        for row in xrange(1, len_row + 1):
            for col in xrange(1, len_col + 1):
                dp[row][col] = dp[row][col - 1] + \
                               dp[row - 1][col] - \
                               dp[row - 1][col - 1] + \
                               matrix[row - 1][col - 1]
        
        # check the value of each submatrix. O((m*n)^2)
        for max_row in xrange(len_row):
            for max_col in xrange(len_col):
                end_sum = dp[max_row + 1][max_col + 1]
                for row in xrange(max_row + 1):
                    for col in xrange(max_col + 1):
                        # get the sum from (row, col) to (max_row, max_col)
                        cur_sum = end_sum - (\
                                  dp[max_row + 1][col] + \
                                  dp[row][max_col + 1]) + \
                                  dp[row][col]
                                  
                        if cur_sum == 0:
                            return [(row, col), (max_row, max_col)]
        
        return []
