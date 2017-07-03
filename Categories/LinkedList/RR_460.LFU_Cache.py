"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""

# ============== double linkedlist + ordered dict ==================
# Time: O(1)
# Space: O(3cap)
# Idea:
"""
same as bucket. each bucket store the nodes with same frequency, use double linkedlist to store all buckets.
in order to make each bucket FIFO and del in O(1), use ordered dict to store keys.
move key to the next bucket if next bucket frequency is cur+1, otherwise create a new one.
"""
class Node(object):
    def __init__(self, count):
        self.count = count
        self.keys = collections.OrderedDict()
        self.prev = None
        self.next = None

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.value_hash = {}
        self.node_hash = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.value_hash:
            self.__increase_count(key)
            return self.value_hash[key]
        
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap <= 0:
            return

        if key in self.value_hash:
            self.value_hash[key] = value
        else:
            if len(self.value_hash) >= self.cap:
                self.__pop_lfu()
                
            self.value_hash[key] = value
            self.__add_to_head(key)
            
        self.__increase_count(key)
        
        
    def __increase_count(self, key):
        node = self.node_hash[key]
        cur_count = node.count
        del node.keys[key]
        if len(node.keys) == 0:
            self.__delete_node(node)
            node = node.prev
        
        cur_node = None
        if node.next.count == cur_count + 1:
            cur_node = node.next
        else:
            
            cur_node = Node(cur_count + 1)
            cur_node.next = node.next
            node.next.prev = cur_node
            cur_node.prev = node
            node.next = cur_node
            
        cur_node.keys[key] = None
        self.node_hash[key] = cur_node
            
        
        
    def __pop_lfu(self):
        if self.head.next.count == -1:
            return
        
        first_node = self.head.next
        key, value = first_node.keys.popitem(last=False)
        if len(first_node.keys) == 0:
            self.__delete_node(first_node)

        del self.value_hash[key]
        del self.node_hash[key]
        
        
    def __add_to_head(self, key):
        node = None
        if self.head.next.count == 0:
            node = self.head.next
        else:
            node = Node(0)
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            
        node.keys[key] = None
        self.node_hash[key] = node
        
    def __delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
