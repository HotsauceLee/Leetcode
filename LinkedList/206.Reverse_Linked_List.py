# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        dump = ListNode(-1)
        dump.next = head
        head_save = head
        head = dump
        mid = head.next
        tail = None
        while mid:
            tail = mid.next
            mid.next = head
            head = mid
            mid = tail
        head_save.next = None
            
        return head
