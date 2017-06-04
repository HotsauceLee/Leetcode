"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""

# =============== pointers ============
# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
            
        return dummy.next
