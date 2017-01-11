# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#=============== Bottom-up recursion ================
# Time: O(log(n))
# Space: O(log(n))
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        
        if root.val == key:
            if root.left:
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                left_right_most.right = root.right
                
                return root.left
            else:
                return root.right
                
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root

# ============= Same but change delete to the right smallest node ==========
# Time: O(log(n))
# Space: O(log(n))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        
        if root.val == key:
            if not root.right:
                return root.left
            else:
                right_smallest = root.right
                while right_smallest.left:
                    right_smallest = right_smallest.left
                root.val = right_smallest.val
                root.right = self.deleteNode(root.right, right_smallest.val)
                
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root


”“”
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        
        # Delete root
        if root.val == key:
            if root.left and root.right:
                # Find smallest node in right child
                right_left_most, right_left_most_prev = root.right, root
                while right_left_most.left:
                    right_left_most_prev = right_left_most
                    right_left_most = right_left_most.left
                # Copy value to root
                root.val = right_left_most.val
                # Delete smallest
                if right_left_most_prev is root:
                    root.right = None
                else:
                    right_left_most_prev.left = None
                # Return new root
                return root
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None
        
        prev = None       
        root_copy = root
        while root:
            if key < root.val:
                prev = root
                root = root.left
            elif key > root.val:
                prev = root
                root = root.right
            else:
                if root.left and root.right:
                    right_left_most, right_left_most_prev = root.right, root
                    while right_left_most.left:
                        right_left_most_prev = right_left_most
                        right_left_most = right_left_most.left
                    root.val = right_left_most.val
                    if right_left_most_prev is root:
                        root.right = None
                    else:
                        right_left_most_prev.left = None
                    return root_copy
                elif root.left:
                    if prev.left is root:
                        prev.left = root.left
                        return root_copy
                    else:
                        prev.right = root.left
                        return root_copy
                elif root.right:
                    if prev.left is root:
                        prev.left = root.right
                        return root_copy
                    else:
                        prev.right = root.right
                        return root_copy
                else:
                    if prev.left is root:
                        prev.left = None
                        return root_copy
                    else:
                        prev.right = None
                        return root_copy
                        
        return root_copy
                
“”“
