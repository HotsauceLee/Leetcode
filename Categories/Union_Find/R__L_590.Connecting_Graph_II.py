"""
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), an edge to connect node a and node b
2. query(a), Returns the number of connected component nodes which include node a.

Have you met this question in a real interview? Yes
Example
5 // n = 5
query(1) return 1
connect(1, 2)
query(1) return 2
connect(2, 4)
query(1) return 3
connect(1, 4)
query(1) return 3
"""

# ============ Union Find ==============
# Time: connect - O(1), query - O(1)
# Space: O(2n)
# Trap: 
#   1. Only increase count when unioning
#   2. Return the count of root, not node
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        self.count = {}
        for n in nodes:
            self.father[n] = n
            self.count[n] = 1
            
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
            self.count[f1] += self.count[f2]
            
    def count_connected(self, node):
        return self.count[node]

class ConnectingGraph2:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.uf = UnionFind(range(1, n + 1))


    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        self.uf.union(a, b)


    # @param {int} a
    # return {int}  the number of nodes connected component
    # which include a node.
    def query(self, a):
        # Write your code here
        return self.uf.count_connected(self.uf.find(a))
