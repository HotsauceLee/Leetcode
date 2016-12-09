# =============== Recursion ================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        
        def helper(root, prev_sum):
            if not root: return
            
            cur_sum = prev_sum + 1
            if cur_sum > result[0]:
                result[0] = cur_sum
                
            left_sum = 0
            if root.left and root.left.val == root.val + 1:
                left_sum = cur_sum
            right_sum = 0
            if root.right and root.right.val == root.val + 1:
                right_sum = cur_sum
                
            helper(root.left, left_sum)
            helper(root.right, right_sum)
            
        helper(root, 0)
        return result[0]
