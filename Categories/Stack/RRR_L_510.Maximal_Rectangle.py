"""
Given a 2D boolean matrix filled with False and True, find the largest rectangle containing all True and return its area.

Have you met this question in a real interview? Yes
Example
Given a matrix:

[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
return 6.
"""

# ============= Increasing Stack ============
# Time: O(row*col + row*2col)
# Space: O(row*col + col)
class Solution:
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    def maximalRectangle(self, matrix):
        # Write your code here
        if not matrix:
            return 0
            
        len_row, len_col = len(matrix), len(matrix[0])
        if len_row < 1 or len_col < 1:
            return 0

        # O(row*col)
        # Put an extra 0 at the end of every row, force pop all elements.
        heights = [[0]*(len_col + 1) for i in xrange(len_row)]
        for r in xrange(len_row):
            for c in xrange(len_col):
                if r == 0:
                    heights[r][c] = matrix[r][c]
                else:
                    heights[r][c] = heights[r-1][c] + 1 if matrix[r][c] == 1 else 0

        # O(row*2col)
        result = 0
        for row in xrange(len_row):
            cur_q = []
            for col in xrange(len_col + 1):
                while cur_q and heights[row][col] < heights[row][cur_q[-1]]:
                    top_idx = cur_q.pop()
                    width = col if not cur_q else col - cur_q[-1] - 1
                    result = max(result, heights[row][top_idx]*width)
                cur_q.append(col)
                    
        return result
