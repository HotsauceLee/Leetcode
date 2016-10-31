# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#================= Recursion =================
# Time: O(n)
# Space: O(n)
# Running time: ~45ms
class Solution(object):
    def zigzagLevelOrder(self, root):
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
            if level % 2 == 0:
                result[level].append(root.val)
            else:
                result[level].insert(0, root.val)
                
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)

#============== Queue with deque =================
# Time: O(n)
# Space: O(n)
# Running time: Same
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        """
        result = []
        if root is None:
            return result
        
        q = deque([root])
        reverse = False
        while len(q) > 0:
            current_level = deque()
            for i in range(len(q)):
                node = q.pop()
                if reverse:
                    current_level.appendleft(node.val)
                else:
                    current_level.append(node.val)
                
                if node.left is not None:
                    q.appendleft(node.left)
                if node.right is not None:
                    q.appendleft(node.right)
            
            result.append(list(current_level))
            reverse = not reverse
                    
        return result
