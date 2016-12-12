#======================== Stack with lat popped =================
# Time: O(n)
# Space: O(log(n))
# Running time: ~50ms
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
            
        stack = [root]
        last_popped = root
        while stack:
            last_node = stack[-1]
            if last_node.left is not None and last_node.left is not last_popped and last_node.right is not last_popped:
                stack.append(last_node.left)
            elif last_node.right is not None and last_node.right is not last_popped:
                result.append(last_node.val)
                stack.append(last_node.right)
            else:
                last_popped = stack.pop()
                if last_popped.right is None:
                    result.append(last_popped.val)
                
        return result
    
# =============== Recursion without global prev =======================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, prev, result):
            if not root: return prev
            
            prev = helper(root.left, prev, result)
            
            result.append(root.val)
            
            prev = helper(root.right, root, result)
            
            return prev
            
        result = []
        helper(root, None, result)
        return result

# ================= Morris Traversal ===================

class Sloution(object):
	def inorderTraversal(self, root):
		result = []
		while root:
			if not root.left:
				result.append(root.val)
				root = root.right
			else:
				# Find predecessor
				predecessor = root.left
				while predecessor.right and predecessor.right is not root:
					predecessor = predecessor.right
					
				if not predecessor.right:
					predecessor.right = root
					root = root.left
				else:
					predecessor.right = None
					result.append(root.val)
					root = root.right

		return result
