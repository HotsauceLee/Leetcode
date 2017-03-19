"""
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b. 2.query(a, b)`, check if two nodes are connected

Have you met this question in a real interview? Yes
Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true
"""

# ========== Union Find ===========
# Time: connect - O(1), query - O(1)
# Space: O(n)
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        for n in nodes:
            self.father[n] = n
        
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
        

class ConnectingGraph:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.uf = UnionFind(range(1, n + 1))


    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        self.uf.union(a, b)


    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self, a, b):
        # Write your code here
        return self.uf.find(a) == self.uf.find(b)
