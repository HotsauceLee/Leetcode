# ================ Only checks whether two elements are in the same set ===================
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
            
            
# =========== Non-recursion find =================
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        for n in nodes:
            self.father[n] = n
        
    def find(self, node):
        if self.father[node] == node:
            return node
        
        f = node
        f = self.father[f]
        while f != self.father[f]:
            f = self.father[f]

        compress = node
        while compress != self.father[compress]:
            compress = self.father[compress]
            self.father[compress] = f

        return f
        
    def union(self, node1, node2):
        f1 = self.find(node1)
        f2 = self.find(node2)
        if f1 != f2:
            self.father[f2] = f1

# ================ Keep the number of subsets ===================
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        self.count = 0
        for n in nodes:
            self.father[n] = n
            self.count += 1
        
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
            self.count -= 1
            
    def subset_count(self):
        return self.count
    
# =============== Keeps the elements of each subset =============
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        self.fathers = {}
        for n in nodes:
            self.father[n] = n
            self.fathers[n] = [n]

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
            self.father[f1] = f2
            self.fathers[f2] += self.fathers[f1]
            del self.fathers[f1]
            
    def subsets(self):
        return self.fathers
