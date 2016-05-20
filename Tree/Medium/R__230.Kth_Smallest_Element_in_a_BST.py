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
# Running time: 76ms
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


######## Resursion ##############
# BTS, count the # of node on left side and decide which way to go
# Running time: 
# Time complexity:
# Space complexity: 
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        c = self.count(root.left)
        if k == c + 1:
            return root.val
        if k <= c:
            return self.kthSmallest(root.left, k)
        
        return self.kthSmallest(root.right, k - 1 - c)
            

    def count(self, root):
        if root is None:
            return 0
            
        return 1 + self.count(root.left) + self.count(root.right)
        
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
# A: Modify tree node object to have both left and right node count, and do BTS to find the kth.
# When inserting/deleting, update the node count of either side when traversing the tree.
# Time complexity: O(height)
# Space complexity: O(height)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.left_count = 0
#         self.right = None
#         self.right_count = 0
