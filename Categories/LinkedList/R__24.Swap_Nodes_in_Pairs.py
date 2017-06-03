"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

# =============== pointers ==============
# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        begin, end = dummy, head.next.next
        while True:
            first = begin.next
            second = begin.next.next
            
            begin.next = second
            second.next = first
            first.next = end
            
            if not end or not end.next:
                break
            begin = first
            end = end.next.next
            
        return dummy.next
            
# ================ recursion ====================
# Time: O(n)
# Space: O(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        
        return n
