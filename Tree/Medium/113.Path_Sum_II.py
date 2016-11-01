# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# ================== Recursion =================
# Time: O(n)
# Space: O(n)
# Running time: ~80ms
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(root, sum, [], result)
        return result
        
    def helper(self, root, sum, cur_path, result):
        if root is None:
            return
        
        cur_path.append(root.val)
        minus_self = sum - root.val
        if minus_self == 0 and root.left is None and root.right is None:
            result.append(cur_path)
            return
            
        self.helper(root.left, minus_self, cur_path[:], result)
        self.helper(root.right, minus_self, cur_path[:], result)
