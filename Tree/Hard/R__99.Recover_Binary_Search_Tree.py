# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    prev = TreeNode(-sys.maxint - 1)
    node1 = None
    node2 = None
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
        
    def helper(self, root):
        if not root:
            return
        
        self.helper(root.left)
        
        if not self.node1 and self.prev.val >= root.val:
            self.node1 = self.prev
        if self.node1 and self.prev.val >= root.val:
            self.node2 = root
        self.prev = root
        self.helper(root.right)

#============== Morris Traversal =======================
# TODO:
