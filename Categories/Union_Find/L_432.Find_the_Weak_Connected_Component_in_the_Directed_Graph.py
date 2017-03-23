"""
Find the number Weak Connected Component in the directed graph. Each node in the graph contains a label and a list of its neighbors. (a connected set of a directed graph is a subgraph in which any two vertices are connected by direct edge path.)

 Notice

Sort the element in the set in increasing order

Have you met this question in a real interview? Yes
Example
Given graph:

A----->B  C
 \     |  | 
  \    |  |
   \   |  |
    \  v  v
     ->D  E <- F
Return {A,B,D}, {C,E,F}. Since there are two connected component which are {A,B,D} and {C,E,F}

"""

# ================ Union Find =================
# Time: O(n^2 + n^2 + nlog(n)) n - total # of nodes
# Space: O(2n)
class UnionFind(object):
    def __init__(self, father, fathers):
        self.father = father
        self.fathers = fathers
        
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
            self.fathers[f2] += self.fathers[f1]
            del self.fathers[f1]
            
    def f(self):
        return self.fathers

# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        if not nodes:
            return []
        
        father = {}
        fathers = {}
        # O(n^2)
        for n in nodes:
            father[n.label] = n.label
            fathers[n.label] = [n.label]
            for neighbor in n.neighbors:
                father[neighbor.label] = neighbor.label
                fathers[neighbor.label] = [neighbor.label]
        
        uf = UnionFind(father, fathers)
        # O(n^2)
        for n in nodes:
            for neighbor in n.neighbors:
                uf.union(n.label, neighbor.label)
                
        regions = uf.f().values()
        result = []
        for r in regions:
            # O(nlogn)
            result.append(sorted(r))
        return result
