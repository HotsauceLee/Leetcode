# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#================ Recursion =================
# Time: O(n)
# Space: O(n)
# Running Time: ~40ms
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)
        
    def helper(self, root, prev):
        if root is None:
            return 0
            
        plus_self = prev*10 + root.val
        if root.left is None and root.right is None:
            return plus_self
        
        return self.helper(root.left, plus_self) + self.helper(root.right, plus_self)

# dfs + stack
def sumNumbers1(self, root):
    if not root:
        return 0
    stack, res = [(root, root.val)], 0
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right:
                res += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
    return res
    
# bfs + queue
def sumNumbers2(self, root):
    if not root:
        return 0
    queue, res = collections.deque([(root, root.val)]), 0
    while queue:
        node, value = queue.popleft()
        if node:
            if not node.left and not node.right:
                res += value
            if node.left:
                queue.append((node.left, value*10+node.left.val))
            if node.right:
                queue.append((node.right, value*10+node.right.val))
    return res
