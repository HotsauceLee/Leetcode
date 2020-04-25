"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        From each building do BFS and record how many steps to reach each cell.
        NOTE: Used Pruning in BFS. If didn't see all other houses in a BFS run,
        that means this house is blocked therefore could immediately return -1.
        
        House means building.
        
        T: O(M*N)
        S: O(M*N)
        """
        if not grid or not grid[0]: return 0
        row_count = len(grid)
        col_count = len(grid[0])
        
        houses = []
        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == 1:
                    houses.append((row, col))
                    
        
        visited = [[0]*col_count for _ in range(row_count)]
        def bfs(row, col):
            cur_visited = [[False]*col_count for _ in range(row_count)]
            cur_visited[row][col] = True
            q = collections.deque([(row, col)])
            houses_saw = 1
            degree = 1
            while q:
                cur_level = len(q)
                for _ in range(cur_level):
                    cur_r, cur_c = q.popleft()
                    # up
                    up_r, up_c = cur_r - 1, cur_c
                    if up_r >= 0 and not cur_visited[up_r][up_c]:
                        if grid[up_r][up_c] == 1:
                            houses_saw += 1
                        elif grid[up_r][up_c] != 2:
                            cur_visited[up_r][up_c] = True
                            visited[up_r][up_c] += 1
                            grid[up_r][up_c] -= degree
                            q.append((up_r, up_c))
                    # down
                    down_r, down_c = cur_r + 1, cur_c
                    if down_r < row_count and not cur_visited[down_r][down_c]:
                        if grid[down_r][down_c] == 1:
                            houses_saw += 1
                        elif grid[down_r][down_c] != 2:
                            cur_visited[down_r][down_c] = True
                            visited[down_r][down_c] += 1
                            grid[down_r][down_c] -= degree
                            q.append((down_r, down_c))
                    # left
                    left_r, left_c = cur_r, cur_c - 1
                    if left_c >= 0 and not cur_visited[left_r][left_c]:
                        if grid[left_r][left_c] == 1:
                            houses_saw += 1
                        elif grid[left_r][left_c] != 2:
                            cur_visited[left_r][left_c] = True
                            visited[left_r][left_c] += 1
                            grid[left_r][left_c] -= degree
                            q.append((left_r, left_c))
                    # right
                    right_r, right_c = cur_r, cur_c + 1
                    if right_c < col_count and not cur_visited[right_r][right_c]:
                        if grid[right_r][right_c] == 1:
                            houses_saw += 1
                        elif grid[right_r][right_c] != 2:
                            cur_visited[right_r][right_c] = True
                            visited[right_r][right_c] += 1
                            grid[right_r][right_c] -= degree
                            q.append((right_r, right_c))
                    
                degree += 1
                
            return houses_saw
        
        for h in houses:
            houses_saw = bfs(h[0], h[1])
            if houses_saw < len(houses): return -1  
                    
        min_dist = float('inf')
        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] < 0 and visited[row][col] == len(houses):
                    min_dist = min(min_dist, abs(grid[row][col]))
        
        # for [[1]] case, where we saw all houses but there are no space
        return min_dist if min_dist < float('inf') else -1
