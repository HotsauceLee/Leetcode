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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return self.bfs(n, edges)
    
    def bfs(self, n, edges):
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
