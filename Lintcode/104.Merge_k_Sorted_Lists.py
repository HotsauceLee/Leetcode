# ============= Heap + Custom Object ================
# Time: O(Nlog(N) + N) N = all nodes
# Space: O(1)
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Node(object):
    def __init__(self, node=None):
        self.node = node
        
    def __cmp__(self, other):
        return self.node.val - other.node.val

import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, Node(l))
                l = l.next
        
        dummy = ListNode(-1)
        cursor = dummy
        while heap:
            new_node = heapq.heappop(heap)
            cursor.next = new_node.node
            cursor = cursor.next
            
        return dummy.next
        

