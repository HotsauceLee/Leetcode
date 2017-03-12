# ============== Set row and col to None ==========
# Time: O((mn)^2)
# Space: O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        len_row = len(matrix)
        len_col = len(matrix[0])
        
        for row in xrange(len_row):
            for col in xrange(len_col):
                # If was 1, turn to 2
                if matrix[row][col] == 0:
                    # Update entire row
                    for r in xrange(len_row):
                        if matrix[r][col] != 0:
                            matrix[r][col] = None
                    # Update entire col
                    for c in xrange(len_col):
                        if matrix[row][c] != 0:
                            matrix[row][c] = None
        # Recover
        for row in xrange(len_row):
            for col in xrange(len_col):
                if not matrix[row][col]:
                    matrix[row][col] = 0
                    
                    
# ================ Use first row and col to store the state of that row or col
# Time: O(mn)
# Space: O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        col0, len_row, len_col = matrix[0][0], len(matrix), len(matrix[0])
        for row in xrange(len_row):
            if matrix[row][0] == 0:
                col0 = 0
            for col in xrange(1, len_col):
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0
                    
        for row in xrange(1, len_row):
            for col in xrange(1, len_col):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
                    
        if matrix[0][0] == 0:
            for col in xrange(len_col):
                matrix[0][col] = 0
        if col0 == 0:
            for row in xrange(len_row):
                matrix[row][0] = 0
