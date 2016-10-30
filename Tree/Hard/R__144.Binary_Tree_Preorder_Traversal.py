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


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val) 
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)

        return ' '.join(vals)


    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())
        return doit()

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
            print [node.val for node in stack]
            last_node = stack[-1]
            if last_node.left is not None and last_node.left is not last_popped and last_node.right is not last_popped:
                stack.append(last_node.left)
                result.append(last_node.left.val)
            elif last_node.right is not None and last_node.right is not last_popped:
                stack.append(last_node.right)
                result.append(last_node.right.val)
            else:
                stack.pop()
                
        return result

tree_str = "5 3 2 # # 4 # # 7 6 # # 8 # #"
decoder = Codec()
root = decoder.deserialize(tree_str) 

decoder.preorderTraversal(root)
