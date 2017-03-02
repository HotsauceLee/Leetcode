# ========== DP ===========
# Time: O(m*n)
# Space: O(1)
class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid:
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0
            
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        if row == 0 or col == 0:
            return 0
            
        for r in xrange(row):
            if obstacleGrid[r][0] == 0:
                obstacleGrid[r][0] = -1
            if obstacleGrid[r][0] == 1:
                break
                
        for c in xrange(col):
            if obstacleGrid[0][c] == 0:
                obstacleGrid[0][c] = -1
            if obstacleGrid[0][c] == 1:
                break
                
        for r in xrange(1, row):
            for c in xrange(1, col):
                if obstacleGrid[r][c] == 1:
                    continue
                
                from_up = 0
                if obstacleGrid[r - 1][c] != 1:
                    from_up = obstacleGrid[r - 1][c]
                from_left = 0
                if obstacleGrid[r][c - 1] != 1:
                    from_left = obstacleGrid[r][c - 1]
                    
                obstacleGrid[r][c] = from_up + from_left
                
        return -obstacleGrid[-1][-1]
