"""
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

 Notice

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Have you met this question in a real interview? Yes
Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].
"""

# ============== Union Find ===============
# Time: O(m*n + o) o - # of operators
# Space: O(2mn)
class UnionFind(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.father = range(n*m)
        self.land = [0]*(n*m)
        self.count = 0
        self.delta_x = [0, 0, 1, -1]
        self.delta_y = [1, -1, 0, 0]
        
    def find(self, node):
        if self.father[node] == node:
            return node
            
        f = self.find(self.father[node])
        self.father[node] = f
        return f
        
    def union(self, n1, n2):
        f1 = self.find(n1)
        f2 = self.find(n2)
        if f1 != f2:
            self.father[f1] = f2
            self.count -= 1
            
    def __inbound(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m
            
    def add(self, node):
        cur_x, cur_y = node.x, node.y
        cur_node = cur_x*self.m + cur_y
        if self.land[cur_node]:
            return

        self.land[cur_node] = 1
        self.count += 1
        for i in xrange(len(self.delta_x)):
            next_x = cur_x + self.delta_x[i]
            next_y = cur_y + self.delta_y[i]
            next_node = next_x*self.m + next_y
            if self.__inbound(next_x, next_y) and self.land[next_node]:
                self.union(cur_node, next_node)
                
    def query(self):
        return self.count
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Point[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        if not operators:
            return []
            
        uf = UnionFind(n, m)
        result = []
        for o in operators:
            uf.add(o)
            result.append(uf.query())
            
        return result
