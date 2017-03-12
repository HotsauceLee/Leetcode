# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: 72ms
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
            
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        if l == 0:
            return r + 1
        if r == 0:
            return l + 1
        
        return l + 1 if l <= r else r + 1

######## Queue ##############
# Running time: 68ms
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        q = [root]
        current_level = 1
        while len(q) > 0:
            nodes_count = len(q)
            for i in range(nodes_count):
                current_node = q.pop()
                if current_node.left is None and current_node.right is None:
                    return current_level
                if current_node.left is not None:
                    q.insert(0, current_node.left)
                if current_node.right is not None:
                    q.insert(0, current_node.right)
            current_level += 1
            
        return current_level