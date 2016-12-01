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
    def __init__(self, key=None, value=None):
        self.key = key
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
            node = self.d[key]
            node.val = value
            self.move_to_head(key)
            return
        
        if self.vol >= self.cap:
            self.pop()
            self.vol -= 1
        
        new_node = self.append(key, value)
        self.d[key] = new_node
        self.vol += 1
            
        
        
    def move_to_head(self, key):
        value_node = self.d[key]
        self.remove(key)
        self.append(key, value_node.val)
        
    def remove(self, key):
        node = self.d[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.vol -= 1
        
    def append(self, key, value):
        node = DLL(key, value)
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        self.vol += 1
        
        return node
        
    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None
        self.vol -= 1
        
        
l2 = LRUCache2(2)
#l2.set(1, 1)
#l2.set(2, 2)
#print "l2.get(1): " + str(l2.get(1))
#l2.set(3, 3)
#print "l2.get(2): " + str(l2.get(2))
#print "l2.get(3): " + str(l2.get(3))
l2.set(2,1)
l2.set(1,1)
l2.get(2)
l2.set(4,1)
l2.get(1)
l2.get(2)
