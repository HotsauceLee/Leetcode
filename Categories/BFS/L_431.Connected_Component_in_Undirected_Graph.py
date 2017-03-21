"""
Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

 Notice

Each connected component should sort by label.

Have you met this question in a real interview? Yes
Clarification
Learn more about representation of graphs

Example
Given graph:

A------B  C
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}
"""

# ================ BFS ==================
# Time: O(n^2 + n + nlog(n)). n-total # of nodes
# Space: O(n + n)
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        if not nodes:
            return []
            
        all_nodes = set()
        for n in nodes:
            all_nodes.add(n)
            for neighbor in n.neighbors:
                all_nodes.add(neighbor)
        
        result = []
        q = collections.deque()
        while all_nodes:
            first_node = all_nodes.pop()
            sub_result = []
            q.appendleft(first_node)
            all_nodes.discard(first_node)
            while len(q) > 0:
                cur_len = len(q)
                for i in xrange(cur_len):
                    cur_node = q.pop()
                    sub_result.append(cur_node.label)
                    for neighbor in cur_node.neighbors:
                        if neighbor in all_nodes:
                            all_nodes.discard(neighbor)
                            q.appendleft(neighbor)
            sub_result.sort()
            result.append(sub_result)
            
        return result
                
        
