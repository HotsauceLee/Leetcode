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
# Time: O(n)
# Space: O(1)
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        node1 = None
        node2 = None
        prev = None
        while root:
            if not root.left:
                if not node1 and prev and root.val <= prev.val:
                    node1 = prev
                if node1 and root.val <= prev.val:
                    node2 = root
                prev = root
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    predecessor.right = None
                    if not node1 and prev and root.val <= prev.val:
                        node1 = prev
                    if node1 and root.val <= prev.val:
                        node2 = root
                    prev = root
                    root = root.right
                    
        node1.val, node2.val = node2.val, node1.val
