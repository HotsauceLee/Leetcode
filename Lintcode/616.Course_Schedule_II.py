"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Have you met this question in a real interview? Yes
Example
Given n = 2, prerequisites = [[1,0]]
Return [0,1]

Given n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
Return [0,1,2,3] or [0,2,1,3]
"""
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
