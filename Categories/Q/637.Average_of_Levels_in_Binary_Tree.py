"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# =============== deque ===============
# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = collections.deque([root])
        result = []
        while q:
            cur_level_len = len(q)
            cur_sum = 0
            for i in xrange(cur_level_len):
                cur_node = q.pop()
                cur_sum += cur_node.val
                if cur_node.right:
                    q.appendleft(cur_node.right)
                if cur_node.left:
                    q.appendleft(cur_node.left)
                    
            result.append(cur_sum*1.0/cur_level_len)
            
        return result
        
