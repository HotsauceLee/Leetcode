"""
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Have you met this question in a real interview? Yes
Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 
return the node 1.
"""
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
