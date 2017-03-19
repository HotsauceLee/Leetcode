"""
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Have you met this question in a real interview? Yes
Example
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.
"""

# =============== Union Find ===============
# Time: O(2*m*n)
# Space: O(m*n)
# Trap:
#   1. initialize count with the # of 1
#   2. row*len_col + col could generate unique number for all cells
#   3. use list instead of dict could save a little bit of time
class UnionFind(object):
    def __init__(self, nodes):
        self.father = []
        for n in xrange(nodes):
            self.father.append(n)
            
    def set_count(self, c):
        self.count = c
        
    def query(self):
        return self.count
            
    def find(self, node):
        if self.father[node] == node:
            return node
            
        f = self.find(self.father[node])
        self.father[node] = f
        return f
        
    def union(self, node1, node2):
        f1 = self.find(node1)
        f2 = self.find(node2)
        if f1 != f2:
            self.father[f2] = f1
            self.count -= 1
            

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0
        
        len_row = len(grid)
        len_col = len(grid[0])
        
        uf = UnionFind(len_row*len_col)
        count = 0
        for row in grid:
            count += row.count(1)
        uf.set_count(count)
        
        delta_x = [0, 0, 1, -1]
        delta_y = [1, -1, 0, 0]

        def in_bound(x, y):
            return 0 <= x < len_row and 0 <= y < len_col
            
        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                if grid[row][col] == 1:
                    for i in xrange(len(delta_x)):
                        next_row = row + delta_x[i]
                        next_col = col + delta_y[i]
                        if in_bound(next_row, next_col) and grid[next_row][next_col] == 1:
                            uf.union(row*len_col + col, next_row*len_col + next_col)
                            
        return uf.query()
        
