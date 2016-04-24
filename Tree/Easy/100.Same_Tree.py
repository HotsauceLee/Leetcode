# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######## Resursion ##############
# Running time: 56ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

######## Queue ##############
# Running time: 56ms
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        q1 = [p]
        q2 = [q]
        while len(q1) > 0 and len(q2) > 0:
            n1 = q1.pop()
            n2 = q2.pop()
            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False
                
            q1.insert(0, n1.left)
            q2.insert(0, n2.left)
            q1.insert(0, n1.right)
            q2.insert(0, n2.right)
            
        return True