# See tree
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
