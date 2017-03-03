# ============= Recursion =============
# Time: O(n)
# Space: O(n)
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    def findSubtree(self, root):
        # Write your code here
        def helper(r, result):
            if not r: return 0
                
            l_sum = helper(r.left, result)
            r_sum = helper(r.right, result)
            cur_sum = l_sum + r_sum + r.val
            if cur_sum < result[0]:
                result[0], result[1] = cur_sum, r
            
            return cur_sum
            
        result = [float('inf'), None]
        helper(root, result)
        return result[1]
