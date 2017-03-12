# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#================== Recurison ==================
# Time: O(n)
# Space: O(n)
# Running time: ~200ms
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
            
        root = TreeNode(preorder[0])
        del preorder[0]
        inorder_idx = inorder.index(root.val)
        
        root.left = self.buildTree(preorder, inorder[:inorder_idx])
        root.right = self.buildTree(preorder, inorder[inorder_idx + 1:])
        
        return root
