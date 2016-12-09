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

# ================ Stack ====================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        result = 0
        stack = [(root, 1)]
        while stack:
            (cur_node, cur_sum) = stack.pop()
            if cur_sum > result: result = cur_sum
            if cur_node.left:
                if cur_node.left.val == cur_node.val + 1:
                    stack.append((cur_node.left, cur_sum + 1))
                else:
                    stack.append((cur_node.left, 1))
            if cur_node.right:
                if cur_node.right.val == cur_node.val + 1:
                    stack.append((cur_node.right, cur_sum + 1))
                else:
                    stack.append((cur_node.right, 1))
                
        return result
