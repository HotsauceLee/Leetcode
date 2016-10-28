# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#=============== Stack ====================
# Time: hasNext: O(1) next:
# Space: O(h)
# Explaination: The average time complexity of next() function is O(1) indeed in your case. As the next function can be called n times at most, and the number of right nodes in self.pushAll(tmpNode.right) function is maximal n in a tree which has n nodes, so the amortized time complexity is O(1). 
class BSTIterator(object):
    stack = []
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            return
        
        self.stack.append(root)
        l = root.left
        while l:
            self.stack.append(l)
            l = l.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) > 0:
            return True
            
        return False

    def next(self):
        """
        :rtype: int
        """
        smallest = self.stack.pop()
        r = smallest.right
        if r is not None:
            self.stack.append(r)
            l = r.left
            while l:
                self.stack.append(l)
                l = l.left
            
        return smallest.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
