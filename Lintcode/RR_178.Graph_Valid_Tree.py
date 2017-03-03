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
