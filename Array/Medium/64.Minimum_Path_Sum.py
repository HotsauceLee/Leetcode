# ============ DP ============
# Time: O(m + n + m*n)
# Space: O(1)
# Idea: grid[m][n] = min(up, left) + grid[m][n]
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h, w = len(grid), len(grid[0])
        
        for first_row in xrange(1, w):
            grid[0][first_row] += grid[0][first_row - 1]
        for first_col in xrange(1, h):
            grid[first_col][0] += grid[first_col - 1][0]
        
        for i in xrange(1, h):
            for j in xrange(1, w):
                if 
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[h - 1][w - 1]

# ========== Better ============
# Time: O(m*n)
# Space: O(1)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[0])):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i != 0 and j != 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[-1][-1]
