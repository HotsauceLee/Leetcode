# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: 68ms
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        return l + 1 if l >= r else r + 1


######## Level Traversal ##############
# Running time: 64ms
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        q = [root]
        max_depth = 0
        current_level = 0
        while len(q) > 0:
            current_level = len(q)
            for i in range(current_level):
                current_node = q.pop()
                if current_node.left is not None:
                    q.insert(0, current_node.left)
                if current_node.right is not None:
                    q.insert(0, current_node.right)
                    
            max_depth += 1
            
        return max_depth