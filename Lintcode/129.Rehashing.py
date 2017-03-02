# =============== Loops ================
# Time: O(N = all nodes)
# Space: O(2N)
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        if not hashTable:
            return None
                
        new_cap = len(hashTable)*2
        new_table = [None]*(new_cap)
        for node in hashTable:
            while node:
                new_idx = node.val % (new_cap)
                if not new_table[new_idx]:
                    new_table[new_idx] = ListNode(node.val)
                else:
                    head = new_table[new_idx]
                    while head.next:
                        head = head.next
                    head.next = ListNode(node.val)
                node = node.next
                    
        return new_table   
