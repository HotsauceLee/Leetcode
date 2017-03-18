"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""

# ================= BFS =================
# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        result = []
        q = collections.deque([root])
        while any(q):
            cur_level = len(q)
            cur_biggest = float('-inf')
            for i in xrange(cur_level):
                cur_node = q.pop()
                cur_biggest = max(cur_biggest, cur_node.val)
                if cur_node.left:
                    q.appendleft(cur_node.left)
                if cur_node.right:
                    q.appendleft(cur_node.right)
            result.append(cur_biggest)

        return result
