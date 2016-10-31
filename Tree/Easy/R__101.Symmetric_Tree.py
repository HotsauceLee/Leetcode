# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: 52ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, root)
        
        
    def helper(self, root1, root2):
        if root1 is None and root2 is None: return True
        if root1 is None or root2 is None: return False
        if root1.val != root2.val: return False
        
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)


######## Queue ##############
# Running time: 56ms
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root, root]
        while len(q) > 0:
            node1 = q.pop()
            node2 = q.pop()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
                
            q.insert(0, node1.left)
            q.insert(0, node2.right)
            q.insert(0, node1.right)
            q.insert(0, node2.left)
                
        return True