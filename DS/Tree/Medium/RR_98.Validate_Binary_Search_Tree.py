# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion with min and max ##############
# Running time: 72ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -sys.maxint - 1, sys.maxint)
        
    def helper(self, root, min, max):
        if root is None:
            return True
            
        if ((root.left is not None and root.left.val >= root.val) or root.val >= max):
            return False
            
        if ((root.right is not None and root.right.val <= root.val) or root.val <= min):
            return False
            
        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)


######## Resursion with prev ##############
# Running time: 72ms
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    prev = None

    def isValidBST(self, root):
        if root is None:
            return True
            
        if not self.isValidBST(root.left):
            return False
            
        if (self.prev is not None) and (self.prev.val >= root.val):
            return False
        
        self.prev = root
        return self.isValidBST(root.right)
