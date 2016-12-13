# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#=================== Stack Destroy original tree===================
# Time: O(n)
# Space: O(log(n))
# Running time: ~40ms
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        
        stack = [root]
        while stack:
            last_node = stack[-1]
            if last_node.left is not None:
                stack.append(last_node.left)
                last_node.left = None
                continue
            
            if last_node.right is not None:
                stack.append(last_node.right)
                last_node.right = None
                continue
            
            cur_node = stack.pop()
            result.append(cur_node.val)
            
        return result
        

#==================== Stack with last popped ==================
# Time: O(n)
# Space: O(log(n))
# Running time: ~35ms
class Solution(object):
    def postorderTraversal(self, root):
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
            top_node = stack[-1]
            # Push left
                # top.left is not null && top.left is not last_popped && top.right is not last_popped
            # Push right
                # top.right is not null && top.right is not lst_popped && (top.left is null || top.left is last_popped)
            # Otherwise Pop

            if top_node.left is not None and top_node.left is not last_popped and top_node.right is not last_popped:
                stack.append(top_node.left)
			elif top_node.right is not None and top_node.right is not last_popped:
                stack.append(top_node.right)
            else:
                last_node = stack.pop()
                last_popped = last_node
                result.append(last_node.val)
                
        return result

# ================== Morris Traversal using extra space ===================
# Time: O(n)
# Space: (n)
from collections import deque
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        dump = TreeNode(-1)
        dump.left = root
        while dump:
            if not dump.left:
                dump = dump.right
            else:
                predecessor = dump.left
                while predecessor.right and predecessor.right is not dump:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = dump
                    dump = dump.left
                else:
                    predecessor.right = None
                    # Put reverse values in to a tmp list
                    # then attach it to the end of result
                    reverse = deque()
                    frm = dump.left
                    while frm:
                        reverse.appendleft(frm.val)
                        frm = frm.right
                    result += list(reverse)
                    dump = dump.right
                    
        return result

# ================== Morris Traversal ===================
# Time: O(n)
# Space: (1)
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        dump = TreeNode(-1)
        dump.left = root
        while dump:
            if not dump.left:
                dump = dump.right
            else:
                predecessor = dump.left
                while predecessor.right and predecessor.right is not dump:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = dump
                    dump = dump.left
                else:
                    self.store_reverse(dump.left, predecessor, result)
                    dump = dump.right
                    
        return result
        
    def reverse(self, frm, to):
        if frm is to: return
        nxt = frm.right
        tail = None
        while frm is not to:
            tail = nxt.right
            nxt.right = frm
            frm = nxt
            nxt = tail
            
    def store_reverse(self, frm, to, result):
        self.reverse(frm, to)
        while True:
            result.append(to.val)
            if to is frm: break
            to = to.right
        self.reverse(to, frm)
