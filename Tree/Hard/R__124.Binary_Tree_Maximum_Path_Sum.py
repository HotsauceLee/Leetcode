# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# =============== Recursion ================
# Time: O(n)
# Space: O(n)
# Idea: (1) computes the maximum path sum with highest node is the input node, update maximum if necessary 
#       (2) returns the maximum sum of the path that can be extended to input node's parent.
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_val = -sys.maxint - 1
        self.helper(root)
        return self.max_val

    def helper(self, root):
        if root is None:
            return 0
            
        l = max(0, self.helper(root.left))
        r = max(0, self.helper(root.right))
        
        self.max_val = max(self.max_val, l + r + root.val)
        return max(l, r) + root.val
        
