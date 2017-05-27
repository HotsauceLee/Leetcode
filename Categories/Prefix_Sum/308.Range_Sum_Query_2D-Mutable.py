"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

# ============== sums array ==============
# Time: init - O(m*n) update - O(m*n) sumRegion - O(1)
# Space: O(m*n)
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return

        self.m = matrix
        self.len_row, self.len_col = len(matrix), len(matrix[0])
        self.sums = [[0]*(self.len_col + 1) for i in xrange(self.len_row + 1)]
        
        for row in xrange(1, self.len_row + 1):
            for col in xrange(1, self.len_col + 1):
                self.sums[row][col] = self.sums[row - 1][col] + \
                                      self.sums[row][col - 1] - \
                                      self.sums[row - 1][col - 1] + \
                                      matrix[row - 1][col - 1]
                                      
        self.updates = collections.OrderedDict()

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if row < 0 or row >= self.len_row or col < 0 or col >= self.len_col:
            return
        
        old = self.m[row][col]
        for r in xrange(row, self.len_row):
            for c in xrange(col, self.len_col):
                self.sums[r + 1][c + 1] = self.sums[r + 1][c + 1] - old + val
        
        self.m[row][col] = val
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = self.sums[row2 + 1][col2 + 1] - \
                 self.sums[row1][col2 + 1] - \
                 self.sums[row2 + 1][col1] + \
                 self.sums[row1][col1]
                 
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
