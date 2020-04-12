"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
class UnionFind:
    def __init__(self, nodes):
        self.fathers = {}
        self.unique_sets = len(nodes)
        for n in nodes:
            self.fathers[n] = n
            
    def find(self, node, compress=True):
        if self.fathers[node] == node: return node

        # find the real father
        f = node
        while self.fathers[f] != f:
            f = self.fathers[f]
        
        # Recursion method sets the father of all
        # nodes along the path to the new father.
        # In order to do the same in non-recursive
        # version, we need to iterate the path
        # again and set them manually.
        if compress:
            node_clone = node
            while self.fathers[node_clone] != node_clone:
                node_clone = self.fathers[node_clone]
                self.fathers[node_clone] = f
                
        self.fathers[node] = f
        return f
    
    def union(self, node1, node2):
        f1 = self.find(node1)
        f2 = self.find(node2)
        if f1 != f2:
            self.fathers[f1] = f2
            self.unique_sets -= 1
            

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 0: return 0
        if not edges: return n
        
        #return self.bfs(n, edges)
        return self.union_find(n, edges)
    
    def bfs(self, n, edges):
        """
        Expand from each unvisited node and count.
        T: O(N) - visit each node once
        S: O(N) - worst case all nodes except root are in the q
        """
        neighbors = collections.defaultdict(list)
        for begin, end in edges:
            neighbors[begin].append(end)
            neighbors[end].append(begin)
        not_visited = set(range(n))
        result = 0
        
        while not_visited:
            node = not_visited.pop()
            q = collections.deque([node])
            while q:
                cur_level = len(q)
                for _ in range(cur_level):
                    cur_node = q.popleft()
                    not_visited.discard(cur_node)
                    for n in neighbors.get(cur_node, []):
                        # this could prevent going back
                        if n in not_visited: q.append(n)
            result += 1
            
        return result
    
    def union_find(self, n, edges):
        uf = UnionFind(range(n))
        for begin, end in edges:
            uf.union(begin, end)
            
        return uf.unique_sets
