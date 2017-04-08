"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

Have you met this question in a real interview? Yes
Example
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""

# ============ DP =============
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        if not matrix:
            return 0

        len_row, len_col = len(matrix), len(matrix[0])
        dp = [[0]*len_col for i in xrange(len_row)]
        
        def inbound(r, c):
            return 0 <= r < len_row and 0 <= c < len_col

        max_area = 0
        for row in xrange(len_row):
            for col in xrange(len_col):
                dp[row][col] = [0, 0]
                if matrix[row][col] == 0:
                    continue

                # up
                up_row, up_col = row - 1, col
                dp[row][col][1] = dp[up_row][up_col][1] + 1 if inbound(up_row, up_col) else 1
                # left
                left_row, left_col = row, col - 1
                dp[row][col][0] = dp[left_row][left_col][0] + 1 if inbound(left_row, left_col) else 1

                # record max area
                if inbound(row - 1, col - 1):
                    matrix[row][col] = min(matrix[row - 1][col - 1] + 1, min(dp[row][col][0], dp[row][col][1]))

                max_area = max(max_area, matrix[row][col]**2)

        return max_area
