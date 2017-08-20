"""
Given a node from a cyclic linked list which has been sorted, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be any single node in the list. Return the inserted new node.

 Notice

3->5->1 is a cyclic list, so 3 is next node of 1.
3->5->1 is same with 5->1->3

Have you met this question in a real interview? Yes
Example
Given a list, and insert a value 4:
3->5->1
Return 5->1->3->4
"""
# ==========================
# Time: O(n)
# Space: O(1)
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param {ListNode} node a list node in the list
    # @param {int} x an integer
    # @return {ListNode} the inserted new list node
    def insert(self, node, x):
        # Write your code here
        new_node = ListNode(x)
        if not node:
            new_node.next = new_node
            return new_node
            
        node_save = node
        while True:
            if node.val <= x <= node.next.val:
                break
            if node.val > node.next.val and (node.val < x or x < node.next.val):
                break
            
            node = node.next
            if node is node_save:
                break
            
        new_node.next = node.next
        node.next = new_node
        return new_node
