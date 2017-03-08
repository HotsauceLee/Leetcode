# ================== Dict ======================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        entry_point = RandomListNode(-1)
        prev = entry_point
        cur = head
        d = {}
        while cur:
            # Next
            if d.has_key(cur):
                prev.next = d[cur]
                new_node = prev.next
            else:
                new_node = RandomListNode(cur.label)
                d[cur] = new_node
                prev.next = new_node
            
            # Random
            if not cur.random:
                new_node.random = None
            elif d.has_key(cur.random):
                new_node.random = d[cur.random]
            else:
                new_random = RandomListNode(cur.random.label)
                d[cur.random] = new_random
                new_node.random = new_random
                
            cur = cur.next
            prev = prev.next
            
        return entry_point.next
    
# ================= Pointer-put new node between old ones =================
# Time: O(n)
# Space: O(1)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Copy list
        step1_head = head
        while step1_head:
            next = step1_head.next
            new_node = RandomListNode(step1_head.label)
            step1_head.next = new_node
            new_node.next = next
            step1_head = next
            
        # Random
        step2_head = head
        while step2_head:
            if step2_head.random:
                step2_head.next.random = step2_head.random.next
            step2_head = step2_head.next.next
            
        # Restore
        entry_point = RandomListNode(-1)
        prev = entry_point
        while head:
            old_next = head.next.next
            new_head = head.next
            head.next = old_next
            
            prev.next = new_head
            prev = new_head
            head = head.next
            
        return entry_point.next
