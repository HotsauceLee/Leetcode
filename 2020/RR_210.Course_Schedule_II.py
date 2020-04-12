"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses <= 0:
            return []
        if not prerequisites:
            return range(numCourses)

        #return self.topological_sort(numCourses, prerequisites)
        return self.dfs(numCourses, prerequisites)
    
    def topological_sort(self, numCourses, prerequisites):
        """
        https://en.wikipedia.org/wiki/Topological_sorting
        T: O(N) - visit all node once
        S: O(N) - worst case all node are heads
        """
        outgoing = collections.defaultdict(list)
        incoming = collections.defaultdict(int)
        result = collections.deque()
        for p in prerequisites:
            outgoing[p[0]].append(p[1])
            incoming[p[1]] += 1

        # the ones in outgoing but have no incoming edges are heads
        heads = collections.deque(set(outgoing.keys()) - set(incoming.keys()))
        all_nodes = set(range(numCourses))

        while heads:
            h = heads.popleft()
            result.appendleft(h)
            all_nodes.discard(h)
            for n in outgoing[h]:
                incoming[n] -= 1
                if incoming[n] == 0:
                    del incoming[n]
                    heads.append(n)

        return list(all_nodes) + list(result) if not incoming else []
    
    def dfs(self, numCourses, prerequisites):
        """
        Global stack to build result in each dfs.
        If hit a node we have already visited before,
        that means we have visited all it's neighbors
        either, so we don't put it into the stack.
        
        For loops, keep track of current path. If hit
        already visited node in current path then error out.
        
        T: O(N) - visited each node once
        S: O(N) - all_visited(N) + helper worst case(N)
        """
        edges = collections.defaultdict(list)
        for p in prerequisites:
            edges[p[0]].append(p[1])
        result = []
        all_visited = set()
            
        def helper(c, visited):
            nonlocal edges
            nonlocal result
            nonlocal all_visited
            if c in all_visited: return
            all_visited.add(c)
            
            for n in edges.get(c, []):
                if n in visited: raise RuntimeError
                visited.add(n)
                helper(n, visited)
                visited.remove(n)
            
            # append to the beginning of stack
            result.append(c)
        
        try:
            # iterate all courses in case some with no
            # neighbors are the prerequists of about to
            # be visited ones.
            for c in range(numCourses):
                # mark c visited before going in
                helper(c, set([c]))
            return result
        except RuntimeError:
            return []
