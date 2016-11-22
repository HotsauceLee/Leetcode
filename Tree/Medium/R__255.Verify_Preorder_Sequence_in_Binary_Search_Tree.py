class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
		
	def helper(self, min_val, max_val, preorder, inorder):
		if not inorder: return 

		val = preorder[0]
		del preorder[0]
		if val < min_val or val > max_val: return False
		idx = inorder.index(val)

		l = self.helper(min_val, val, preorder, inorder[:idx])
		r = self.helper(val, max_val, preorder, inorder[idx + 1:])
		
		return l and r

