"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# ============ Sort all nodes =============
# Time: O(n + nlog(n) + n)
# Space: O(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not list:
            return None
        
        def list_node_comparator(n1, n2):
            return n1.val - n2.val
        
        heap = []
        # O(n)
        for l in lists:
            while l:
                heap.append(l)
                l = l.next
        
        # O(nlog(n))
        heap.sort(cmp=list_node_comparator)
        dummy = ListNode(0)
        head = dummy
        # O(n)
        for node in heap:
            head.next = node
            head = head.next
        head.next = None
        return dummy.next
