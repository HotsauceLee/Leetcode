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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        q = collections.deque([root])
        result = []
        while q:
            cur_level = len(q)
            cur_max = float('-inf')
            for _ in range(cur_level):
                node = q.popleft()
                cur_max = max(node.val, cur_max)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(cur_max)
            
        return result
