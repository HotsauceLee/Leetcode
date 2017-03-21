# ============== Union Find ==============
# Time: O(n^2 + n + n^2 + nlogn). n - total # of nodes
# Space: O(2n(uf) + n(node set))
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        # key is to keep track the regions by father
        self.fathers = {}
        for n in nodes:
            self.father[n] = n
            self.fathers[n] = [n]

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
            self.father[f1] = f2
            self.fathers[f2] += self.fathers[f1]
            del self.fathers[f1]
            
    def subsets(self):
        return self.fathers

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        all_nodes = set()
        # O(n^2)
        for n in nodes:
            all_nodes.add(n.label)
            for neighbor in n.neighbors:
                all_nodes.add(neighbor.label)
        
        # O(n)
        uf =  UnionFind(all_nodes)
        # O(n^2)
        for n in nodes:
            for neighbor in n.neighbors:
                uf.union(n.label, neighbor.label)
                
        regions = uf.subsets()
        # O(n) ~ O(nlogn)
        result = []
        for r in regions.values():
            r.sort()
            result.append(r)
            
        return result
