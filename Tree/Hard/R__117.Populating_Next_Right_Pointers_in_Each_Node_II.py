# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#============== Pointers =================
# Time: O(n)
# Space: O(1)
# Running time: ~90ms
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        
        cur = root
        next_left = None
        while cur:
			start = None
			while cur:
				if cur.left:
					if not next_left:
						next_left = cur.left
					else:
						start.next = cur.left

					start = cur.left

				if cur.right:
					if not next_left:
						next_left = cur.right
					else:
						start.next = cur.right
					start = cur.right

				cur = cur.next
			cur = next_left
			next_left = None
