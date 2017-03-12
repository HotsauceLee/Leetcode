# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ############
# Best time: 44ms
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        left_child = root.left 
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left_child)
        
        return root


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######### Level Traversal ########
# Best time: 40ms
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
            
        q = [root]
        while len(q) > 0:
            current_level = len(q)
            for i in range(current_level):
                current_node = q.pop()
                current_node.left, current_node.right = current_node.right, current_node.left
                if current_node.left is not None:
                    q.insert(0, current_node.left)
                if current_node.right is not None:
                    q.insert(0, current_node.right)
                    
        return root