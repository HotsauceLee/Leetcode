# ============== Recursion ================
# Time: O(n)
# Space: O(n)
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
import copy
class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """ 
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        def helper(root, A, B):
            if not root: return None, False, False
            
            l, l_found_A, l_found_B = helper(root.left, A, B)
            r, r_found_A, r_found_B = helper(root.right, A, B)
            
            found_A = l_found_A or r_found_A or root is A
            found_B = l_found_B or r_found_B or root is B
            
            if root is A or root is B or (l and r):
                return root, found_A, found_B
                
            return l or r, found_A, found_B
            
        lca, A_exist, B_exist = helper(root, A, B)
        return lca if A_exist and B_exist else None
