# =============== Two stacks ===================
# Time: O(n + k)
# Space: O(n)
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # inorder
        s1 = []
        self.inorder(root, False, target, s1)
        # reverse inorder
        s2 = []
        self.inorder(root, True, target, s2)
        
        result = []
        while k > 0:
            if not s1: result.append(s2.pop())
            elif not s2: result.append(s1.pop())
            elif abs(float(s1[-1]) - target) < abs(float(s2[-1]) - target): result.append(s1.pop())
            else: result.append(s2.pop())
            k -= 1
            
        return result
        
    def inorder(self, root, reverse, target, s):
        if not root: return
    
        self.inorder(root.right if reverse else root.left, reverse, target, s)
        
        if (reverse and root.val <= target) or (not reverse and root.val > target): return
        s.append(root.val)
        
        self.inorder(root.left if reverse else root.right, reverse, target, s)
