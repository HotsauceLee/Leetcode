"""
Given a list of Connections, which is the Connection class (the city name at both ends of the edge and a cost between them), find some edges, connect all the cities and spend the least amount.
Return the connects if can connect all the cities, otherwise return empty list.

 Notice

Return the connections sorted by the cost, or sorted city1 name if their cost is same, or sorted city2 if their city1 name is also same.

Have you met this question in a real interview? Yes
Example
Gievn the connections = ["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]

Return ["Acity","Bcity",1], ["Acity","Ccity",2]
"""

# =============== Union Find ================
# Time: O(nlogn + e + e) n - total # of nodes. e - # of edges
# Space: O(n)
# Idea:
"""
http://www.jianshu.com/p/04ca0fc1afab
https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
"""

class UnionFind(object):
    def __init__(self, d):
        self.father = d
        self.count = len(d)
        
    def __find(self, c):
        if self.father[c] == c:
            return c
            
        f = self.__find(self.father[c])
        self.father[c] = f
        return f
        
    def union(self, c1, c2):
        f1 = self.__find(c1)
        f2 = self.__find(c2)
        if f1 != f2:
            self.father[f1] = f2
            self.count -= 1
            return True
        return False
        
    def query(self):
        return self.count

'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        if not connections:
            return []
            
        def connection_cmp(c1, c2):
            if c1.cost != c2.cost:
                return c1.cost - c2.cost
            if c1.city1 != c2.city1:
                return 1 if c1.city1 > c2.city1 else -1
            if c1.city2 != c2.city2:
                return 1 if c1.city2 > c2.city2 else -1
            return 0
        
        # O(nlogn)
        connections.sort(cmp=connection_cmp)
        d = {}
        # O(e)
        for n in connections:
            if n.city1 not in d:
                d[n.city1] = n.city1
            if n.city2 not in d:
                d[n.city2] = n.city2

        uf = UnionFind(d)
        result = []
        # O(e)
        for n in connections:
            if uf.union(n.city1, n.city2):
                result.append(n)

        return result if uf.query() == 1 else []
