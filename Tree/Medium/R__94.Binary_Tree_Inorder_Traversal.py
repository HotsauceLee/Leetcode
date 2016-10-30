# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#======================== Stack with lat popped =================
# Time: O(n)
# Space: O(log(n))
# Running time: ~50ms
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
            
        stack = [root]
        last_popped = root
        while stack:
            last_node = stack[-1]
            if last_node.left is not None and last_node.left is not last_popped and last_node.right is not last_popped:
                stack.append(last_node.left)
            elif last_node.right is not None and last_node.right is not last_popped:
                result.append(last_node.val)
                stack.append(last_node.right)
            else:
                last_popped = stack.pop()
                if last_popped.right is None:
                    result.append(last_popped.val)
                
        return result
