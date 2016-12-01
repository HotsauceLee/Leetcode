from collections import deque

class LRUCache1(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.d = {}
        self.idx = deque()
    
    # O(n) - remove
    def get(self, key):
        """
        :rtype: int
        """
        if not self.d.has_key(key): return -1
        
        self.push_to_head(key)
        return self.d[key]

    # O(n) - remove
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        # Set
        if self.d.has_key(key):
            self.d[key] = value
            self.push_to_head(key)
            return
        
        # Insert
        if len(self.idx) >= self.cap:
            idx_delete = self.idx.pop()
            del self.d[idx_delete]

        self.d[key] = value
        self.idx.appendleft(key)
        
    def push_to_head(self, key):
        self.idx.remove(key)
        self.idx.appendleft(key)
        
        
class DLL(object):
    def __init__(self, value=None):
        self.val = value
        self.prev = None
        self.next = None

class LRUCache2(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        h = DLL()
        t = DLL()
        h.next = t
        t.prev = h
        
        self.vol = 0
        self.cap = capacity
        self.d = {}
        self.head = h
        self.tail = t
        

    def get(self, key):
        """
        :rtype: int
        """
        if self.d.has_key(key):
            node = self.d[key]
            self.move_to_head(key)
            return node.val
            
        return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.cap <= 0: reutrn
        if self.d.has_key(key):
            new_node = DDL(value)
            self.d[key] = new_node
            self.move_to_head(key)
            return
        
        if self.vol >= self.cap:
            self.pop()
            self.vol -= 1
        
        self.append(key, DLL(value))
        self.vol += 1
            
        
        
    def move_to_head(self, key):
        node = self.remove(key)
        self.append(key, node)
        
        
        
        
    def remove(self, key):
        node = self.d[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.vol -= 1
        
        return node
        
    def append(self, key, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        self.vol += 1
        
    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None
        self.vol -= 1
        
        
