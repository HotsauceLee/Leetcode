"""
Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

 Notice

You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.
Have you met this question in a real interview? Yes
Example
Given a grid:

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
return 8, You can build at (1,1). (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)
"""
# ============= BFS ================
# Time: O(n)
# Sapce: O(n)
class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid: return 0
        
        def bfs():
            degree = 1
            q = collections.deque([(x, y)])
            visited = [[False]*w for i in xrange(h)]
            while len(q) > 0:
                cur_len = len(q)
                for i in xrange(cur_len):
                    cur_x, cur_y = q.pop()
                    if cur_x + 1 < h and grid[cur_x + 1][cur_y] <= 0 and not visited[cur_x + 1][cur_y]:
                        grid[cur_x + 1][cur_y] -= degree
                        visited[cur_x + 1][cur_y] = True
                        visited_count[cur_x + 1][cur_y] += 1
                        q.appendleft((cur_x + 1, cur_y))
                    if cur_x - 1 >= 0 and grid[cur_x - 1][cur_y] <= 0 and not visited[cur_x - 1][cur_y]:
                        grid[cur_x - 1][cur_y] -= degree
                        visited[cur_x - 1][cur_y] = True
                        visited_count[cur_x - 1][cur_y] += 1
                        q.appendleft((cur_x - 1, cur_y))
                    if cur_y + 1 < w and grid[cur_x][cur_y + 1] <= 0 and not visited[cur_x][cur_y + 1]:
                        grid[cur_x][cur_y + 1] -= degree
                        visited[cur_x][cur_y + 1] = True
                        visited_count[cur_x][cur_y + 1] += 1
                        q.appendleft((cur_x, cur_y + 1))
                    if cur_y - 1 >= 0 and grid[cur_x][cur_y - 1] <= 0 and not visited[cur_x][cur_y - 1]:
                        grid[cur_x][cur_y - 1] -= degree
                        visited[cur_x][cur_y - 1] = True
                        visited_count[cur_x][cur_y - 1] += 1
                        q.appendleft((cur_x, cur_y - 1))
                        
                degree += 1
                
        h, w = len(grid), len(grid[0])
        visited_count = [[0]*w for i in xrange(h)]
        house_count = 0
        for x in xrange(h):
            for y in xrange(w):
                if grid[x][y] == 1:
                    house_count += 1
                    bfs()
        
        min_dist = float('inf')
        for x in xrange(h):
            for y in xrange(w):
                if visited_count[x][y] == house_count and grid[x][y] < 0:
                    min_dist = min(min_dist, abs(grid[x][y]))
                    
        return min_dist if min_dist < float('inf') else -1
