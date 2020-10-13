# ================ Only checks whether two elements are in the same set ===================
# Trap: when doing union, change father2's father to father1, NOT node2's father to father1!!!!
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        for n in nodes:
            self.father[n] = n

    def add(self, node):
        """
        Add node as we go, don't need all nodes
        during initialization.
        """
        if node not in self.father:
            self.father[node] = node
        
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

    def add(self, node):
        """
        Add node as we go, don't need all nodes
        during initialization.
        """
        if node not in self.father:
            self.father[node] = node
        
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
        
    def add(self, node):
        """
        Add node as we go, don't need all nodes
        during initialization.
        """
        if node not in self.father:
            self.father[node] = node
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

    
# =============== Memorization, amortized O(1) on find and union =============
# 1. Mark the true root of each node in find
# 2. Keep track of the size of each set, make bigger set the root of smaller set to reduce tree height
class UnionFind:
    def __init__(self, n):
        self.size = [1]*n
        self.parent = list(range(n))
    
    def find(self, n):
        if self.parent[n] == n:
            return n
        
        root = n
        while self.parent[root] != root:
            root = self.parent[root]
        
        # memorization, mark the true root of each node
        while n != root:
            old_root = self.parent[n]
            self.parent[n] = root
            n = old_root
            
        return root
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        
        if self.size[p1] >= self.size[p2]:
            self.parent[p2] = self.parent[p1]
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = self.parent[p2]
            self.size[p2] += self.size[p1]

        return True
