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
# Time: O(n)
# Space: O(1)
# Idea:
#	1. If no left child, take root val and go to right
#	2. if left child, find the predecessor.
#		2.1 If no predecessor.right, that means it hasn't been
#			visited yet, attach root to its right.
#		2.2 If predecessor.right, that means it has been
#			visited, set its right back to None.
#	3. Repeat 1 and 2.
# Time Complexity:
"""
时间复杂度：O(n)。证明时间复杂度为O(n)，最大的疑惑在于寻找中序遍历下二叉树中所有节点的前驱节点的时间复杂度是多少，即以下两行代码：

1 while (prev->right != NULL && prev->right != cur)
2     prev = prev->right;
直觉上，认为它的复杂度是O(nlgn)，因为找单个节点的前驱节点与树的高度有关。但事实上，寻找所有节点的前驱节点只需要O(n)时间。n个节点的二叉树中一共有n-1条边，整个过程中每条边最多只走2次，一次是为了定位到某个节点，另一次是为了寻找上面某个节点的前驱节点，如下图所示，其中红色是为了定位到某个节点，黑色线是为了找到前驱节点。所以复杂度为O(n)。
"""
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
