# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    kth = 0
    result = 0
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.kth = k
        self.helper(root)
        
        return self.result
        
    def helper(self, root):
        if root is None:
            return
        
        self.helper(root.left)
        
        if self.kth == 1:
            self.result = root.val
            self.kth -= 1
            return
        self.kth -= 1
        
        self.helper(root.right)
