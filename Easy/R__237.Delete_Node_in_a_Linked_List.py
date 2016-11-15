# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#================ Pointers ===============
# Time: O(n)
# Space: O(1)
# Ideas:
# 	1. Swap values until the end.
# 	2. Copy value fron the next node, then point to the next next one.
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        while next_node:
            node.val = next_node.val
            if not next_node.next:
                break
            
            node = node.next
            next_node = node.next
            
        node.next = None
        
        """
        # no tail case?
        def deleteNode(self, node):
            node.val = node.next.val
            node.next = node.next.next
        """
