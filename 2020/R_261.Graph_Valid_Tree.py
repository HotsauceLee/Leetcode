"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""

class Solution:
    """
    A tree should have exactly n - 1 edges, return if that's not the case
    
    BSF traverse the entire graph, should hit all nodes, If not then some nodes are disconnected, return false.
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #return self.bfs(n, edges)
        return self.union_find(n, edges)
    
    def bfs(self, n, edges):
        # A tree should have exactly n - 1 edges
        if not n or len(edges) != n - 1: return False
        
        d = []
        visited = []
        for _ in range(n):
            d.append([])
            visited.append(False)
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
            
        q = collections.deque([0])
        visited[0] = True
        been = 0
        while q:
            node = q.pop()
            been += 1
            for neighbor in d[node]:
                if not visited[neighbor]:
                    q.appendleft(neighbor)
                    visited[neighbor] = True
                    
        return been == n
    
    def union_find(self, n, edges):
        if len(edges) != n - 1:
            return False
        
        uf = UnionFind(n)
        for e in edges:
            if not uf.union(e[0], e[1]):
                return False
            
        return True
    
    
class UnionFind:
    def __init__(self, n):
        self.size = [1]*n
        self.parent = list(range(n))
    
    def find(self, n):
        if self.parent[n] == n:
            return n
        
        root = n
        while self.parent[root] != root:
            root = self.parent[root]
        
        # memorization, mark the true root of each node
        while n != root:
            old_root = self.parent[n]
            self.parent[n] = root
            n = old_root
            
        return root
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        
        if self.size[p1] >= self.size[p2]:
            self.parent[p2] = self.parent[p1]
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = self.parent[p2]
            self.size[p2] += self.size[p1]

        return True
