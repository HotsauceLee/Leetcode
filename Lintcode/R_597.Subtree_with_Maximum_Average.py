"""
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

Have you met this question in a real interview? Yes
Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
return the node 11.


"""
# ============= Recursion ==============
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
    # @return {TreeNode} the root of the maximum average of subtree
    def findSubtree2(self, root):
        # Write your code here
        def helper(r, result):
            if not r: return 0, 0
                
            l_sum, l_count = helper(r.left, result)
            r_sum, r_count = helper(r.right, result)
            cur_avg = (l_sum + r_sum + r.val)/((l_count + r_count + 1)*1.0)
            if cur_avg > result[0]:
                result[0], result[1] = cur_avg, r
            
            return l_sum + r_sum + r.val, l_count + r_count + 1
            
        result = [float('-inf'), None]
        helper(root, result)
        return result[1]
