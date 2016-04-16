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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
            
        next_val = sum - root.val
        if next_val == 0 and root.left is None and root.right is None:
            return True
        
        return self.hasPathSum(root.left, next_val) or self.hasPathSum(root.right, next_val)