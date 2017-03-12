# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Level Traversal ##############
# Running time: 48ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def levelOrder(self, root):
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
            for i in range(len(q)):
                node = q.pop()
                current_level.append(node.val)
                if node.left is not None:
                    q.insert(0, node.left)
                if node.right is not None:
                    q.insert(0, node.right)
            result.append(current_level)
                    
        return result

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: 60ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.helper(root, 0, result)
        
        return result
        
    def helper(self, root, level, result):
        if root is None:
            return
        
        if level > len(result) - 1:
            result.append([root.val])
        else:
            result[level].append(root.val)
            
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)