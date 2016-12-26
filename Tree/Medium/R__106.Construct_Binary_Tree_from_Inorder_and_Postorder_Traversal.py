# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

#===================== Recursion =====================
# Time: O(n)
# Space: O(n) 
# Running time: ~230ms

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root

#=============== Same but use pointers ================
# Time: O(n)
# Space: O(n) - won't copy lists every time
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(i_begin, i_end):
            if i_begin > i_end or p_end[0] < 0: return None
            
            root = TreeNode(postorder[p_end[0]])
            p_end[0] -= 1
            root_index = inorder.index(root.val)
            root.right = helper(root_index + 1, i_end)
            root.left = helper(i_begin, root_index - 1)
            
            return root
        
        p_end = [len(postorder) - 1]
        return helper(0, len(inorder) - 1)
