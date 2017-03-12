# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#============= queue level order ===========
# Time: O(n)
# Space: O(n)
# Running time: ~55ms 
# Idea: Get the most right side one of level
class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
            
        q = [root]
        result = []
        while q:
            result.append(q[0].val)
            l = len(q)
            for i in range(l):
                cur_node = q.pop()
                if cur_node.left is not None:
                    q.insert(0, cur_node.left)
                if cur_node.right is not None:
                    q.insert(0, cur_node.right)
                    
        return result
   
#============== Recurison reverse pre-order ============
# Time: O(n)
# Space: O(n)
# Running Time: ~50ms
# Idea: Compare current depth and length of the result
#    if depth is bigger, then it is the right most one.
class Solution(object):
   
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, 0, result)
        return result
    
    def helper(self, root, depth, result):
        if root is None:
            return
        
        if depth >= len(result):
            result.append(root.val)
            
        self.helper(root.right, depth + 1, result)
        self.helper(root.left, depth + 1, result)
        
        return
