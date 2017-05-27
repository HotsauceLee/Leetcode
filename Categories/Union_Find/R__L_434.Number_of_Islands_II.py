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

# ============ better =============
# Time: O(k)
# Space: O(k)
class UnionFind(object):
    # O(1)
    def __init__(self):
        self.fathers = {}
        self.count = 0
     
    # O(1)  
    def add(self, n):
        self.fathers[n] = n
        self.count += 1
    
    # Amortized O(1)
    def find(self, n):
        if self.fathers[n] == n:
            return n
            
        f = self.find(self.fathers[n])
        self.fathers[n] = f
        return f
    
    # Amortized O(1)
    def union(self, n1, n2):
        f1 = self.find(n1)
        f2 = self.find(n2)
        if f1 != f2:
            # !!!
            self.fathers[f2] = f1
            self.count -= 1
    
    # O(1)
    def total_count(self):
        return self.count

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m <= 0 or n <= 0 or not positions:
            return 0
        
        d = set()
        uf = UnionFind()
        delta_row = [1, -1, 0, 0]
        delta_col = [0, 0, 1, -1]
        
        def within(row, col):
            return 0 <= row < m and 0 <= col < n

        result = []
        # O(k)
        for p in positions:
            cur_row = p[0]
            cur_col = p[1]
            cur_1d = cur_row*n + cur_col
            if within(cur_row, cur_col) and cur_1d not in d:
                d.add(cur_1d)
                uf.add(cur_1d)
                # O(4)
                for i in xrange(len(delta_row)):
                    next_row = cur_row + delta_row[i]
                    next_col = cur_col + delta_col[i]
                    next_1d = next_row*n + next_col
                    if within(next_row, next_col) and next_1d in d:
                        uf.union(cur_1d, next_1d)
            
            result.append(uf.total_count())
            
        return result
