# Trap: when doing union, change father2's father to father1, NOT node2's father to father1!!!!
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        for n in nodes:
            self.father[n] = n
        
    def find(self, node):
        if self.father[node] == node:
            return node
            
        f = self.find(self.father[node])
        self.father[node] = f
        return f
        
    def union(self, node1, node2):
        f1 = self.find(node1)
        f2 = self.find(node2)
        if f1 != f2:
            self.father[f2] = f1
