"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0 or not prerequisites:
            return True
        #return self.bt(numCourses, prerequisites)
        return self.topological_sort(numCourses, prerequisites)
    
    def topological_sort(self, numCourses, prerequisites):
        """
        L = Empty list that will contain the sorted elements
        S = Set of all nodes with no incoming edge

        while S is non-empty do
            remove a node n from S
            add n to tail of L
            for each node m with an edge e from n to m do
                remove edge e from the graph
                if m has no other incoming edges then
                    insert m into S

        if graph has edges then
            return error   (graph has at least one cycle)
        else 
            return L   (a topologically sorted order)
            
        https://en.wikipedia.org/wiki/Topological_sorting
        """
        outgoing = collections.defaultdict(set)
        incoming = collections.defaultdict(int)
        for p in prerequisites:
            outgoing[p[0]].add(p[1])
            incoming[p[1]] += 1
            
        heads = set(outgoing.keys()) - set(incoming.keys())
        while heads:
            node = heads.pop()
            neighbors = outgoing[node].copy()
            for n in neighbors:
                outgoing[node].remove(n)
                incoming[n] -= 1
                if incoming[n] == 0:
                    heads.add(n)
                    del incoming[n]
                    
        return len(incoming) == 0
        
    
    def bt(self, numCourses, prerequisites):
        """
        Time Complexity:
        Space Complexity:
        """
        d = collections.defaultdict(list)
        for p in prerequisites:
            d[p[0]].append(p[1])
            
        for k in d.keys():
            if not self.__bt_helper(k, d, set(), set()):
                return False
        return True
            
    def __bt_helper(self, k, d, path, visited):
        if k in path: return False
        if k in visited: return True
        
        path.add(k)
        for n in d.get(k, []):
            if not self.__bt_helper(n, d, path, visited):
                return False
        path.remove(k)

        visited.add(k)
        return True
