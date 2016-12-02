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
            print "get({}) return: {}".format(key, node.val)
            print "volumn: {}, cap: {}".format(self.vol, self.cap)
            for i in self.d:
                print "{}, {}".format(i, self.d[i].val) 
            return node.val
            
        print "get({}) return: {}".format(key, -1)
        print "volumn: {}, cap: {}".format(self.vol, self.cap)
        for i in self.d:
            print "{}, {}".format(i, self.d[i].val) 
        return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        print "set({}, {})".format(key, value)
        if self.cap <= 0: reutrn
        if self.d.has_key(key):
            node = self.d[key]
            node.val = value
            self.move_to_head(key)
            print "volumn: {}, cap: {}".format(self.vol, self.cap)
            for i in self.d:
                print "{}, {}".format(i, self.d[i].val)
            return
        
        if self.vol >= self.cap:
            self.pop()
        
        new_node = self.append(key, value)
        self.d[key] = new_node
        print "volumn: {}, cap: {}".format(self.vol, self.cap)
        for i in self.d:
            print "{}, {}".format(i, self.d[i].val)
        
        
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
        del self.d[self.tail.prev.key]
        self.tail = self.tail.prev
        self.tail.next = None

        self.vol -= 1
        
def test():
    print "================= Test Case 0 =================="
    l = LRUCache2(2)
    l.set(1, 1)
    l.set(2, 2)
    l.get(1)
    l.set(3, 3)
    l.get(2)
    l.get(3)

def test1():
    print "================= Test Case 1 =================="
    l2 = LRUCache2(2)
    l2.set(2,1)
    l2.set(1,1)
    l2.get(2)
    l2.set(4,1)
    l2.get(1)
    l2.get(2)

"""
1,[set(2,1),get(2),set(3,2),get(2),get(3)]
"""
def test2():
    print "================= Test Case 2 =================="
    l = LRUCache2(1)
    l.set(2,1)
    l.set(3, 2)
    l.get(2)
    l.get(3)

def test3():
    print "================= Test Case 3 =================="
    l = LRUCache2(10)
    l.set(10,13)
    l.set(3,17)
    l.set(6,11)
    l.set(10,5)
    l.set(9,10)
    l.get(13)
    l.set(2,19)
    l.get(2)
    l.get(3)
    l.set(5,25)
    l.get(8)
    l.set(9,22)
    l.set(5,5)
    l.set(1,30)
    l.get(11)
    l.set(9,12)
    l.get(7)
    l.get(5)
    l.get(8)
    l.get(9)
    l.set(4,30)
    l.set(9,3)
    l.get(9)
    l.get(10)
    l.get(10)
    l.set(6,14)
    l.set(3,1)
    l.get(3)
    l.set(10,11)
    l.get(8)
    l.set(2,14)
    l.get(1)
    l.get(5)
    l.get(4)
    l.set(11,4)
    l.set(12,24)
    l.set(5,18)
    l.get(13)
    l.set(7,23)
    l.get(8)
    l.get(12)
    l.set(3,27)
    l.set(2,12)
    l.get(5)
    l.set(2,9)
    l.set(13,4)
    l.set(8,18)
    l.set(1,7)
    l.get(6)
    l.set(9,29)
    l.set(8,21)
    l.get(5)
    l.set(6,30)
    l.set(1,12)
    l.get(10)
    l.set(4,15)
    l.set(7,22)
    l.set(11,26)
    l.set(8,17)
    l.set(9,29)
    l.get(5)
    l.set(3,4)
    l.set(11,30)
    l.get(12)
    l.set(4,29)
    l.get(3)
    l.get(9)
    l.get(6)
    l.set(3,4)
    l.get(1)
    l.get(10)
    l.set(3,29)
    l.set(10,28)
    l.set(1,20)
    l.set(11,13)
    l.get(3)
    l.set(3,12)
    l.set(3,8)
    l.set(10,9)
    l.set(3,26)
    l.get(8)
    l.get(7)
    l.get(5)
    l.set(13,17)
    l.set(2,27)
    l.set(11,15)
    l.get(12)
    l.set(9,19)
    l.set(2,15)
    l.set(3,16)
    l.get(1)
    l.set(12,17)
    l.set(9,1)
    l.set(6,19)
    l.get(4)
    l.get(5)
    l.get(5)
    l.set(8,1)
    l.set(11,7)
    l.set(5,2)
    l.set(9,28)
    l.get(1)
    l.set(2,2)
    l.set(7,4)
    l.set(4,22)
    l.set(7,24)
    l.set(9,26)
    l.set(13,28)
    l.set(11,26)

#test()
#test1()
#test2()
test3()

text = """
set(10,13),set(3,17),set(6,11),set(10,5),set(9,10),get(13),set(2,19),get(2),get(3),set(5,25),get(8),set(9,22),set(5,5),set(1,30),get(11),set(9,12),get(7),get(5),get(8),get(9),set(4,30),set(9,3),get(9),get(10),get(10),set(6,14),set(3,1),get(3),set(10,11),get(8),set(2,14),get(1),get(5),get(4),set(11,4),set(12,24),set(5,18),get(13),set(7,23),get(8),get(12),set(3,27),set(2,12),get(5),set(2,9),set(13,4),set(8,18),set(1,7),get(6),set(9,29),set(8,21),get(5),set(6,30),set(1,12),get(10),set(4,15),set(7,22),set(11,26),set(8,17),set(9,29),get(5),set(3,4),set(11,30),get(12),set(4,29),get(3),get(9),get(6),set(3,4),get(1),get(10),set(3,29),set(10,28),set(1,20),set(11,13),get(3),set(3,12),set(3,8),set(10,9),set(3,26),get(8),get(7),get(5),set(13,17),set(2,27),set(11,15),get(12),set(9,19),set(2,15),set(3,16),get(1),set(12,17),set(9,1),set(6,19),get(4),get(5),get(5),set(8,1),set(11,7),set(5,2),set(9,28),get(1),set(2,2),set(7,4),set(4,22),set(7,24),set(9,26),set(13,28),set(11,26)
"""

def print_fucking_test_case(text):
    begin = None
    end = None
    for i, c in enumerate(text):
        if c == 's' or c == 'g':
            begin = i
            continue

        if begin and c == ')':
            end = i
            print text[begin:end+1]
            
#print_fucking_test_case(text)

