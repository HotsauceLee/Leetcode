# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def s_helper(root):
            if not root: return
            r.append(str(root.val))
            s_helper(root.left)
            s_helper(root.right)

        r = []
        s_helper(root)
        return ' '.join(r)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dl = data.split()
        root = self.helper(-sys.maxint - 1, sys.maxint, dl)
        return root

    def helper(self, low, high, data_list):
        if not data_list: return None
        first_val = int(data_list[0])
        if first_val < low or first_val > high: return None

        root = TreeNode(first_val)
        del data_list[0]
        root.left = self.helper(low, root.val, data_list)
        root.right = self.helper(root.val, high, data_list)

        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def d(data):
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

tree_str = "5 3 2 # # 4 # # 7 6 # # 8 # #"
tree_root1 = d(tree_str)

codec = Codec()
codec.deserialize(codec.serialize(tree_root1))
