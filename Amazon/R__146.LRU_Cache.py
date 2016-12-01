from collections import deque

class LRUCache(object):

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
