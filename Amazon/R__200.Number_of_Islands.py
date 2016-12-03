class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0: return 0
        column = len(grid[0])
        result = 0
        
        def bfs(r, c):
            if r >= row or r < 0 or c >= column or c < 0:
                return
            if grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)
            
            
        for r in range(row):
            for c in range(column):
                if grid[r][c] == '0':
                    continue
                bfs(r, c)
                result += 1
                
        return result
