# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ############
# Best time: 48ms
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []
        self.helper(root, "", result)
        
        return result
        
    def helper(self, root, current_path, result):
        if root is None:
            return
        
        current_path = current_path + "->%s" % root.val
        if root.left is None and root.right is None:
            result.append(current_path[2:])
            return
        
        self.helper(root.left, current_path, result)
        self.helper(root.right, current_path, result)