# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#=================== Stack ===================
# Time: O(n)
# Space: O(log(n))
# Running time: ~40ms
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        
        stack = [root]
        while stack:
            last_node = stack[-1]
            if last_node.left is not None:
                stack.append(last_node.left)
                last_node.left = None
                continue
            
            if last_node.right is not None:
                stack.append(last_node.right)
                last_node.right = None
                continue
            
            cur_node = stack.pop()
            result.append(cur_node.val)
            
        return result
        
