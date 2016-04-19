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
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
            
        if root.val == p.val or root.val == q.val:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        
        if l is None and r is None:
            return None
            
        if l is not None and r is None:
            return l
                
        if r is not None and l is None:
            return r
                
        return root
