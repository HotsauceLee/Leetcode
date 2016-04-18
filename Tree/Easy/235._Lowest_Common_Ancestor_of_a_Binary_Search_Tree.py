# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Level Traversal ##############
# Senarios:
# 1. ________p____root____q___________
#   return root
# 2. _______p(root)_____q(root)_______
#   return root
# 3. ________p________q_____root______
#   go left
# 4. ____root____p________q___________
#   go right
#
# Running time: 120ms
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        return root