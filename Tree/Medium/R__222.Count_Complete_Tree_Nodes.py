# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: 168ms
# Time complexity: 
# Space complexity: 
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        l_dep = 0
        l = root.left
        while (l is not None):
            l = l.left
            l_dep += 1
        r_dep = 0
        r = root.right
        while (r is not None):
            r = r.right
            r_dep += 1
            
        if l_dep == r_dep:
            return 2**(l_dep + 1) - 1
            
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        