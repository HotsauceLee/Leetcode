"""
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route. 
Return -1 if knight can not reached.

 Notice

source and destination must be empty.
Knight can not enter the barrier.

Have you met this question in a real interview? Yes
Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1
"""
# ============ BFS =============
# Time: O(2n)
# Space: O(n)
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path
    def shortestPath(self, grid, source, destination):
        # Write your code here
        if not grid or not source or not destination:
            return -1
        
        self.max_x = len(grid) - 1
        self.max_y = len(grid[0]) - 1
        
        delta_x = [1, 1, 2, 2,-1,-1,-2,-2]
        delta_y = [2,-2, 1,-1, 2,-2, 1,-1]
        
        grid[source.x][source.y] = True
        q = collections.deque([source])
        steps = 0
        while len(q) > 0:
            cur_len = len(q)
            for i in xrange(cur_len):
                cur_node = q.pop()
                cur_x, cur_y = cur_node.x, cur_node.y
                if cur_x == destination.x and cur_y == destination.y:
                    return steps
                for j in xrange(len(delta_x)):
                    next_x = cur_x + delta_x[j]
                    next_y = cur_y + delta_y[j]
                    if self.in_bound(next_x, next_y) and not grid[next_x][next_y]:
                        if next_x == destination.x and next_y == destination.y:
                            return steps + 1
                        grid[next_x][next_y] = True
                        q.appendleft(Point(next_x, next_y))
                                
            steps += 1
            
        return -1
            
    def in_bound(self, x, y):
        return (0 <= x <= self.max_x) and (0 <= y <= self.max_y)
