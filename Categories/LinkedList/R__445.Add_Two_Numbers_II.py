"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# ================= reverse ==================
# Time: O(m + n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
            
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        carry = False
        dummy = ListNode(0)
        new_head = dummy
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            cur_sum = l1_val + l2_val + 1 if carry else l1_val + l2_val
            if cur_sum > 9:
                carry = True
                cur_sum %= 10
            else:
                carry = False
                
            new_head.next = ListNode(cur_sum)
            
            new_head = new_head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            new_head.next = ListNode(1)
            
        return self.reverse(dummy.next)
        
        
    def reverse(self, head):
        if not head or not head.next:
            return head

        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            
            prev = cur
            cur = next
            
        return prev
            

# ================ Stack ==================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
            
        stack1, stack2 = [], []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
            if l2:
                stack2.append(l2.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        prev, carry = None, False
        while stack1 or stack2:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            cur_sum = val1 + val2 + 1 if carry else val1 + val2
            
            if cur_sum > 9:
                carry = True
                cur_sum %= 10
            else:
                carry = False
            
            new_node = ListNode(cur_sum)
            new_node.next = prev
            prev = new_node
            
        if carry:
            new_head = ListNode(1)
            new_head.next = prev
            return new_head
            
        return prev
            
