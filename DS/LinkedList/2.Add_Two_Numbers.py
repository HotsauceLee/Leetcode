# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#============== Pointers ==============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Could use sum instead, see below
        # sum = 0
        carry = False
        root = ListNode(-1)
        prev = root
        while l1 is not None or l2 is not None:
            # sum /= 10
            cur_val = 1 if carry else 0
            if l1 is not None:
                cur_val += l1.val
                l1 = l1.next
            if l2 is not None:
                cur_val += l2.val
                l2 = l2.next
            
            if cur_val >= 10:
                carry = True
                cur_val -= 10
            else:
                carry = False
            
            # prev.next = ListNode(sum % 10)
            prev.next = ListNode(cur_val)
            prev = prev.next
            
        if carry:
            prev.next = ListNode(1)

        return root.next
                
