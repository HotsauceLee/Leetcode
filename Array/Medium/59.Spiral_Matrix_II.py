# ============ Magic ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        if n == 1:
            return [[1]]
            
        result = [[0]*n for i in xrange(n)]
        cur_num = 1
        min_row = min_col = 0
        max_row = max_col = n - 1
        while min_row <= max_row and min_col <= max_col:
            # Go right
            for c in xrange(min_col, max_col + 1):
                result[min_row][c] = cur_num
                cur_num += 1
            min_row += 1
            
            # Go down
            for d in xrange(min_row, max_row + 1):
                result[d][max_col] = cur_num
                cur_num += 1
            max_col -= 1
            
            # Go left
            for l in xrange(max_col, min_col - 1, -1):
                result[max_row][l] = cur_num
                cur_num += 1
            max_row -= 1
                
            # Go up
            for u in xrange(max_row, min_row - 1, -1):
                result[u][min_col] = cur_num
                cur_num += 1
            min_col += 1
                
        return result
                
                
                
