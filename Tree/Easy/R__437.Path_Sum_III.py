# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#================= Dict + Pre-order ================
# Time: O(n)
# Space: O(n)
# Running time: ~80ms
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.helper(root, sum, 0, {0:1})
        
    def helper(self, root, target, path_sum, d):
        if root is None:
            return 0
        
        path_sum += root.val
        result = 0
        if d.has_key(path_sum - target):
            result += d[path_sum - target]
            
        if d.has_key(path_sum):
            d[path_sum] += 1
        else:
            d[path_sum] = 1
            
        l = self.helper(root.left, target, path_sum, d)
        r = self.helper(root.right, target, path_sum, d)
        d[path_sum] -= 1
            
        return result + l + r

#================== List + Pre-order ===========
# Time O(n*log(n))
# Space: 
# Rumming ~400ms
# Problem: loop through the whole list to update values in every iteration.
class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.helper(root, sum, [])
        
    def helper(self, root, sum, path_sum):
        if root is None:
            return 0
        
        result = 0
        path_sum.append(0)
        for idx, path in enumerate(path_sum):
            plus_self = path + root.val
            if plus_self == sum:
                result += 1
            path_sum[idx] = plus_self
           
        return result + self.helper(root.left, sum, path_sum[:]) + self.helper(root.right, sum, path_sum[:])
