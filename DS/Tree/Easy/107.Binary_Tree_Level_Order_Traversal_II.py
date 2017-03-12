# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Level traversal ##############
# Running time: 66ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
            
        result = []
        q = [root]
        while len(q) > 0:
            current_level = []
            level_length = len(q)
            for i in range(level_length):
                current_node = q.pop()
                current_level.append(current_node.val)
                if current_node.left is not None:
                    q.insert(0, current_node.left)
                if current_node.right is not None:
                    q.insert(0, current_node.right)
                    
            result.insert(0, current_level)
            
        return result