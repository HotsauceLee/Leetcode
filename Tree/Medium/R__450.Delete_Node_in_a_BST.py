# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#=============== Bottom-up recursion ================
# Time: O(log(n))
# Space: O(log(n))
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        
        if root.val == key:
            if root.left:
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                left_right_most.right = root.right
                
                return root.left
            else:
                return root.right
                
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root
