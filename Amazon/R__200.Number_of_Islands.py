# ================= DFS =======================
# Time: O(n)
# Space: O(n)
# Running time: ~120ms
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
        
        def dfs(r, c):
            if r >= row or r < 0 or c >= column or c < 0 or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
            
        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    dfs(r, c)
                    result += 1
                
        return result
