# ================== Binary search ====================
# Time: O(log(n))
# Space: O(1)
class Solution(object):
    prev = (None, 0)
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result = root.val
        while root:
            if abs(float(root.val) - target) < abs(float(result) - target):
                result = root.val
                
            root = root.left if root.val > target else root.right
            
        return result
