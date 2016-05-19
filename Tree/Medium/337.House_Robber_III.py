# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: very large ms
# Time complexity: 
# Space complexity: 

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        val1 = 0
        
        if root.left is not None:
            val1 += self.rob(root.left.left) +  self.rob(root.left.right)
           
        if root.right is not None:
            val1 += self.rob(root.right.left) +  self.rob(root.right.right)
            
        return max((root.val +val1), (self.rob(root.left) + self.rob(root.right)))

######## DP + Resursion ##############
# Running time: very large ms
# Time complexity: 
# Space complexity: 
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        map = {}
        return self.robHelper(root, map)
        
        
    def robHelper(self, root, map):
        if root is None:
            return 0
        if map.has_key(root):
            return map[root]
            
        next_next = root.val    
        if root.left is not None:
            next_next += self.robHelper(root.left.left, map) + self.robHelper(root.left.right, map)
        if root.right is not None:
            next_next += self.robHelper(root.right.left, map) + self.robHelper(root.right.right, map)
        
        next = self.robHelper(root.left, map) + self.robHelper(root.right, map)
        
        max_val = max(next_next, next)
        map[root] = max_val
        
        return max_val