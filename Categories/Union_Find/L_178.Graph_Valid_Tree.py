"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

 Notice

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Have you met this question in a real interview? Yes
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
"""

# ============= Union Find ================
# Time: O(e). e - # of edges
# Space: O(n)
class UnionFind(object):
    def __init__(self, n):
        self.father = [0]*n
        self.count = n
        for i in xrange(n):
            self.father[i] = i
            
    def find(self, n):
        if self.father[n] == n:
            return n
            
        f = self.find(self.father[n])
        self.father[n] = f
        return f
        
    def union(self, n1, n2):
        f1 = self.find(n1)
        f2 = self.find(n2)
        if f1 != f2:
            self.father[f1] = f2
            self.count -= 1
            
    def query(self):
        return self.count

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if not n or len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0], e[1])

        return uf.query() == 1
