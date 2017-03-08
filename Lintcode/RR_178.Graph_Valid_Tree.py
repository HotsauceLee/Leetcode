"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

 Notice

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Have you met this question in a real interview? Yes
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.


"""
# ================= BFS ===================
# Time: O(n)
# Space: O(n)
class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if not n or len(edges) != n - 1:
            return False

        d, visited = [], []
        for i in xrange(n):
            d.append([])
            visited.append(False)

        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])

        q = collections.deque([0])
        visited[0] = True
        been = 0
        while len(q) > 0:
            cur = q.pop()
            been += 1
            for neighbor in d[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.appendleft(neighbor)
                    
        return been == n
