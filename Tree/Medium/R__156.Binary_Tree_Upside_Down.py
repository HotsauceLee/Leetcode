# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# ============ Pointer - Find left most first ==============
# Time: O(n)
# Space: O(n)
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        
        stack = []
        left_most = root
        while left_most:
            stack.append(left_most)
            left_most = left_most.left
 
        new_node = TreeNode(-1)    
        prev = new_node
        while stack:
            cur_left = stack.pop()
            prev.right = cur_left
            prev.left = cur_left.right
            
            prev = prev.right
            
        
        prev.left = prev.right = None
        return new_node.right

# ============== Pointer - Better Iteration ==========
# Time: O(n)
# space: O(1)
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        prv = None
        nxt = None
        tmp = None
        
        while cur:
            next = cur.left
            cur.left = tmp
            tmp = cur.right
            cur.right = prv
            
            prv = cur
            cur = next
            
        return prv

# ============== Recurison ================
# Time: O(n)
# Space: O(n)
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root
            
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        
        root.left = root.right = None
        
        return new_root
