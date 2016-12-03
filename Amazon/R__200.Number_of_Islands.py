# ================= DFS =======================
# Time: O(n)
# Space: O(n)
# Running time: ~120ms
class DfsSolution(object):
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

# ================= BFS =======================
# Time: O(n)
# Space: O(n)
# Running time: ~120ms    
from collections import deque

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
            q = deque()
            q.appendleft((r, c))
            grid[r][c] = '0'
            while len(q) > 0:
                cur = q.pop()
                cur_r = cur[0]
                cur_c = cur[1]

                if cur_r + 1 < row and grid[cur_r + 1][cur_c] == '1':
                    q.appendleft((cur_r + 1, cur_c))
                    grid[cur_r + 1][cur_c] = '0'
                if cur_r - 1 >= 0 and grid[cur_r - 1][cur_c] == '1':
                    q.appendleft((cur_r - 1, cur_c))
                    grid[cur_r - 1][cur_c] = '0'
                if cur_c + 1 < column and grid[cur_r][cur_c + 1] == '1':
                    q.appendleft((cur_r, cur_c + 1))
                    grid[cur_r][cur_c + 1] = '0'
                if cur_c - 1 >= 0 and grid[cur_r][cur_c - 1] == '1':
                    q.appendleft((cur_r, cur_c - 1))
                    grid[cur_r][cur_c - 1] = '0'

        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    bfs(r, c)
                    result += 1

        return result
