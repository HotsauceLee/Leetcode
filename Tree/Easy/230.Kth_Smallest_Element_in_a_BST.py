# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: 96ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    
    kth = 0
    result = 0
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.kth = k
        self.helper(root)
        
        return self.result
        
    def helper(self, root):
        if root is None:
            return
        
        self.helper(root.left)
        
        if self.kth == 1:
            self.result = root.val
            self.kth -= 1
            return
        self.kth -= 1
        
        self.helper(root.right)
        
        
######## Stack ##############
# Running time: 84ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [root]
        
        while stack:
            last_node = stack[-1]
            if last_node.left is not None:
                stack.append(last_node.left)
                last_node.left = None
                continue
            
            node = stack.pop()
            if k == 1:
                return node.val
            k -= 1
            
            if node.right is not None:
                stack.append(node.right)
            
        return -1
