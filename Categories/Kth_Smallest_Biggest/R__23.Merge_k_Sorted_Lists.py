"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# ============ Heap ===========
# Time: O(nlog(k)) n - total # of nodes in all lists. k - # of lists
# Space: O(k)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Node(object):
    def __init__(self, list_node):
        self.n = list_node
        
    def __cmp__(self, other):
        return self.n.val - other.n.val

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
            
        heap = []
        for ln in lists:
            if ln:
                heapq.heappush(heap, Node(ln))

        dummy = ListNode(0)
        head = dummy
        while heap:
            cur_smallest = heapq.heappop(heap).n
            head.next = cur_smallest
            head = head.next
            if cur_smallest.next:
                heapq.heappush(heap, Node(cur_smallest.next))
        head.next = None
                
        return dummy.next
            
        
