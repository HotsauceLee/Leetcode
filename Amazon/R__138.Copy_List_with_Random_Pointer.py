# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        entry_point = RandomListNode(-1)
        prev = entry_point
        cur = head
        d = {}
        while cur:
            # Next
            if d.has_key(cur):
                prev.next = d[cur]
                new_node = prev.next
            else:
                new_node = RandomListNode(cur.label)
                d[cur] = new_node
                prev.next = new_node
            
            # Random
            if not cur.random:
                new_node.random = None
            elif d.has_key(cur.random):
                new_node.random = d[cur.random]
            else:
                new_random = RandomListNode(cur.random.label)
                d[cur.random] = new_random
                new_node.random = new_random
                
            cur = cur.next
            prev = prev.next
            
        return entry_point.next
