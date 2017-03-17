"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Have you met this question in a real interview? Yes

"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
            
        # Copy nodes next to the original one
        head_copy_original = head
        while head_copy_original:
            self.copy_node(head_copy_original)
            head_copy_original = head_copy_original.next.next
            
        head_copy_random = head
        while head_copy_random:
            if head_copy_random.random:
                head_copy_random.next.random = head_copy_random.random.next
            head_copy_random = head_copy_random.next.next
                
        # Extract copied list
        dummy = RandomListNode(-1)
        new_head = dummy
        while head:
            new_head.next = head.next
            head.next = head.next.next
            new_head = new_head.next
            head = head.next
            
        return dummy.next
        
    def copy_node(self, node):
        new_node = RandomListNode(node.label)
        new_node.next = node.next
        node.next = new_node
        
    def _print_linkedlist(self, head):
        random = []
        l = ""
        while head:
            l += "%s->" % head.label
            r = head.random.label if head.random else None
            random.append(r)
            head = head.next
        l += "null"
        print l
        print random
        
