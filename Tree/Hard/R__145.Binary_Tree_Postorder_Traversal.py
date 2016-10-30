# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#=================== Stack Destroy original tree===================
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
        

#==================== Stack with last popped ==================
# Time: O(n)
# Space: O(log(n))
# Running time: ~35ms
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

        last_popped = root

        while stack:

            top_node = stack[-1]

            # Push left

                # top.left is not null && top.left is not last_popped && top.right is not last_popped

            # Push right

                # top.right is not null && top.right is not lst_popped && (top.left is null || top.left is last_popped)

            # Otherwise Pop



            if top_node.left is not None and top_node.left is not last_popped and top_node.right is not last_popped:

                stack.append(top_node.left)

            elif top_node.right is not None and top_node.right is not last_popped and (top_node.left is None or top_node.left is last_popped):

                stack.append(top_node.right)

            else:

                last_node = stack.pop()

                last_popped = last_node

                result.append(last_node.val)

                

        return result
