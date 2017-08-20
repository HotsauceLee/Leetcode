"""
Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum sum and the given binary tree is not an empty tree.

Have you met this question in a real interview? Yes
Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5 
return the node with value 3.
"""

# ========== Recursion ============
# Time: O(n)
# Space: O(n)
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the maximum weight node
    def findSubtree(self, root):
        # Write your code here
        self.max_root = None
        self.max_sum = float('-inf')

        def helper(r):
            if not r:
                return 0
            
            l_sum = helper(r.left)
            r_sum = helper(r.right)
            cur_sum = l_sum + r_sum + r.val

            if cur_sum > self.max_sum:
                self.max_root = r
                self.max_sum = cur_sum
                
            return cur_sum
        
        helper(root)
        return self.max_root
