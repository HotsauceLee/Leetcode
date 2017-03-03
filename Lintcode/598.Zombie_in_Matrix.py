# =============== BFS ================
# Time: O(n)
# Space: O(n)
class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        people = 0
        zombies = collections.deque()
        h, w = len(grid), len(grid[0])
        for row in xrange(h):
            for col in xrange(w):
                if grid[row][col] == 0:
                    people += 1
                if grid[row][col] == 1:
                    zombies.append((row, col))
         
        people_infected = 0
        days = 0
        while len(zombies) > 0:
            days += 1
            cur_len = len(zombies)
            for i in xrange(cur_len):
                cur_row, cur_col = zombies.pop()
                if cur_row + 1 < h and grid[cur_row + 1][cur_col] == 0:
                    zombies.appendleft((cur_row + 1, cur_col))
                    grid[cur_row + 1][cur_col] = 1
                    people_infected += 1
                if cur_row - 1 >= 0 and grid[cur_row - 1][cur_col] == 0:
                    zombies.appendleft((cur_row - 1, cur_col))
                    grid[cur_row - 1][cur_col] = 1
                    people_infected += 1
                if cur_col + 1 < w and grid[cur_row][cur_col + 1] == 0:
                    zombies.appendleft((cur_row, cur_col + 1))
                    grid[cur_row][cur_col + 1] = 1
                    people_infected += 1
                if cur_col - 1 >= 0 and grid[cur_row][cur_col - 1] == 0:
                    zombies.appendleft((cur_row, cur_col - 1))
                    grid[cur_row][cur_col - 1] = 1
                    people_infected += 1
            
            if people_infected == people: return days
            
            
        return -1
