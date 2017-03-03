# ============== BFS =================
# Time: O(n)
# Space: o(n)
class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        degree = [0]*numCourses
        edges = [[] for i in xrange(numCourses)]
        
        for p in prerequisites:
            degree[p[0]] += 1
            edges[p[1]].append(p[0])

        q = collections.deque()
        result = []
        for c in xrange(numCourses):
            if degree[c] == 0:
                q.append(c)
                result.append(c)

        while len(q) > 0:
            cur = q.pop()
            for e in edges[cur]:
                degree[e] -= 1
                if degree[e] == 0:
                    result.append(e)
                    q.appendleft(e)
                    
        if len(result) != numCourses:
            return []
                    
        return result
