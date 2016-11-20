# ================= Non Short Circuit OR =============
# TIme: O(n)
# Space: O(n)
class Solution(object):
    count = 0

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root, 0)
        return self.count
        
    def helper(self, root, val):
        if not root: return True
        if (not self.helper(root.left, root.val)) | (not self.helper(root.right, root.val)):
            return False
        self.count += 1
        return root.val == val

class Solution(object):
    def countUnivalSubtrees(self, root):
	def helper(root, count):
	    if not root: return True

	    l = helper(root.left, count)
	    r = helper(root.right, count)

	    if l and r:
		if root.left and root.val != root.left.val:
		    return False
		if root.right and root.val != root.right.val:
		    return False
		count[0] += 1
		return True

	    return False

	count = [0]
	helper(root, count)
    return count[0]
