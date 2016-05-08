# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: 80ms
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.helper(root)
        if result == -1:
            return False
            
        return True
        
            
    def helper(self, root):
        if root is None:
            return 0
            
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l == -1 or r == -1:
            return -1
        
        if abs(l - r) <= 1:
            return l + 1 if l >= r else r + 1
            
        return -1
            
        