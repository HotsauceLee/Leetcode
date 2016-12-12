# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#================== stack with last popped ==============
# Time: O(n)
# Space: O(n)
# Running time: ~35ms
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
            
        stack = [root]
        result.append(root.val)
        last_popped = root
        while stack:
            last_node = stack[-1]
            if last_node.left is not None and last_node.left is not last_popped and last_node.right is not last_popped:
                stack.append(last_node.left)
                result.append(last_node.left.val)
            elif last_node.right is not None and last_node.right is not last_popped:
                stack.append(last_node.right)
                result.append(last_node.right.val)
            else:
                last_popped = stack.pop()
                
        return result

# ============= Morris Traversal ================
# Time: O(n)
# Space: O(1)
# Idea: See 94
class Solution(object):
	def preorderTraversal(self, root):
		result = []
		while root:
			if not root.left:
				result.append(root.val)
				root = root.right
			else:
				predecessor = root.left
				while predecessori.right and predecessor.right is not root:
					predecessor = predecessor.right
				if not predecessor.right:
					predecessor.right = root
					result.append(root.val)
					root = root.left
				else:
					predecessor.right = None
					root = root.right

		return result
