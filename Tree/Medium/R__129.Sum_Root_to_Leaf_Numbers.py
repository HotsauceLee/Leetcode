# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#================ Recursion =================
# Time: O(n)
# Space: O(n)
# Running Time: ~40ms
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)
        
    def helper(self, root, prev):
        if root is None:
            return 0
            
        plus_self = prev*10 + root.val
        if root.left is None and root.right is None:
            return plus_self
        
        return self.helper(root.left, plus_self) + self.helper(root.right, plus_self)
