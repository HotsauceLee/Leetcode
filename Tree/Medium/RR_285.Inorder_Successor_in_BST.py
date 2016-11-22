"""
Hi @xietao0221, let's take the successor for example, basically we always want to find p's closest node (in inorder traversal) and the node's value is larger than p's value, right? That node can either be p's parent or the smallest node in p' right branch.

When the code runs into the else block, that means the current root is either p's parent or a node in p's right branch.

If it's p's parent node, there are two scenarios: 1. p doesn't have right child, in this case, the recursion will eventually return null, so p's parent is the successor; 2. p has right child, then the recursion will return the smallest node in the right sub tree, and that will be the answer.

If it's p's right child, there are two scenarios: 1. the right child has left sub tree, eventually the smallest node from the left sub tree will be the answer; 2. the right child has no left sub tree, the recursion will return null, then the right child (root) is our answer.

I guess it's hard to understand unless you draw different scenarios out. :)
"""
class Solution(object):

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        
        if p.val >= root.val: return self.inorderSuccessor(root.right, p)
        left = self.inorderSuccessor(root.left, p)
        return left if left else root

    def inorderPredecessor(self, root, p):

        if not root: return None
        
        if p.val <= root.val: return self.inorderSuccessor(root.left, p)
        right = self.inorderSuccessor(root.right, p)
        return right if right else root

#============= Pointer inorder Traversal ===========
"""
The inorder traversal of a BST is the nodes in ascending order. To find a successor, you just need to find the smallest one that is larger than the given value since there are no duplicate values in a BST. It just like the binary search in a sorted list. The time complexity should be O(h) where h is the depth of the result node. succ is a pointer that keeps the possible successor. Whenever you go left the current root is the new possible successor, otherwise the it remains the same.

Only in a balanced BST O(h) = O(log n). In the worst case h can be as large as n.
"""
class Solution(object):

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

# =============== Normal Inorder Traversal =============
class Solution(object):
    prev = None
    def inorderSuccessor(self, root, p):
        if not root: return None
        
        l = self.inorderSuccessor(root.left, p)
        if l: return l
        
        if self.prev is p:
            self.prev = root
            return root
            
        self.prev = root
        r = self.inorderSuccessor(root.right, p)
        if r: return r
        
        return None
