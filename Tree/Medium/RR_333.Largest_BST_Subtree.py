# ================ Preorder with min and max ====================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root: return 0, 0, float('inf'), float('-inf')
        
            N1, n1, min1, max1 = helper(root.left)
            N2, n2, min2, max2 = helper(root.right)
            
            n = n1 + n2 + 1 if max1 < root.val < min2 else float('-inf')
            
            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
            
        return helper(root)[0]
