"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# ============== reverse + middle + merge ==============
# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        first, second = self.__split(head)
        second = self.__reverse(second)
        result = self.__merge(first, second)
        
    def __split(self, head):
        slow = fast = head
        # stop when fast doesn't has next
        # then middle is slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None
        return (head, middle)
        
    def __reverse(self, head):
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        return prev
        
    def __merge(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy
        while head1 or head2:
            if head1:
                cur.next = head1
                head1 = head1.next
                cur = cur.next
            if head2:
                cur.next = head2
                head2 = head2.next
                cur = cur.next
                
        return dummy.next
    
    
