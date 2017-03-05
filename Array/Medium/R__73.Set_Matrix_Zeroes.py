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
                    
                    
# ================ 
