# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#============= Return head and tail ==============
# Time: O(n)
# Space: O(n)
# Running time: ~40ms
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
            
    def helper(self, root):
        if root is None:
            return None
            
        l = self.helper(root.left)
        r = self.helper(root.right)
        
        if not l and not r:
            return [root, root]
        
        if not l:
            root.right = r[0]
            return [root, r[1]]
        if not r:
            root.right = l[0]
            root.left = None
            return [root, l[1]]
        
        root.right = l[0]
        root.left = None
        left_tail = l[1]
        left_tail.right = r[0]
        return [root, r[1]]

#============= Postorder Traversal =============
# Time: O(n)
# Space: O(n)
# Running time: Same
class Solution(object):
    prev = None
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
