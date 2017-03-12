# ============ min & max =============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        
        result = []
        min_row, max_row = 0, len(matrix) - 1
        min_col, max_col = 0, len(matrix[0]) - 1
        while min_row <= max_row and min_col <= max_col:
            # right
            for r in xrange(min_col, max_col + 1):
                result.append(matrix[min_row][r])
            min_row += 1
            
            # down
            for r in xrange(min_row, max_row + 1):
                result.append(matrix[r][max_col])
            max_col -= 1
            
            # left
            #[[1,2,3]]
            if max_row >= min_row:
                for l in xrange(max_col, min_col - 1, -1):
                    result.append(matrix[max_row][l])
            max_row -= 1   
                
            # up
            # [[1],[2],[3]]
            if max_col >= min_col:
                for u in xrange(max_row, min_row - 1, -1):
                    result.append(matrix[u][min_col])
            min_col += 1
            
        return result
