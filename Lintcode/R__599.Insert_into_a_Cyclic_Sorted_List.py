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
