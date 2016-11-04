# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#============== Two Pointers ===================
# Time: O(n)
# Space: O(1)
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
		if root is None:
            return
        
        pre = root
        cur = None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
