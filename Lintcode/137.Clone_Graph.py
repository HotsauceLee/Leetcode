# =========== BFS ================
# Time: O(n)
# Space: O(n)
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        if not node: return None
        
        self.dict[node] = UndirectedGraphNode(node.label)
        q = collections.deque([node])
        while len(q) > 0:
            cur_node = q.pop()
            cur_node_copy = self.dict[cur_node]
            for n in cur_node.neighbors:
                if self.dict.has_key(n):
                    cur_node_copy.neighbors.append(self.dict[n])
                else:
                    new_neighbor = UndirectedGraphNode(n.label)
                    self.dict[n] = new_neighbor
                    cur_node_copy.neighbors.append(new_neighbor)
                    q.appendleft(n)
                    
        return self.dict[node]
