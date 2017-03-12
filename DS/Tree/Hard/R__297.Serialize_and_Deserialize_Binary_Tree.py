# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#============= Queue(level order traversal) ======================
# Time: O(n)
# Space: O(n)
# Run time: 400ms+
# Problem: Unknown
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        q = [root]
        result_list = []
        while q:
            l = len(q)
            for i in range(l):
                cur_node = q.pop()
                if cur_node is None:
                    result_list.append('null')
                    continue
                else:
                    result_list.append(str(cur_node.val))

                q.insert(0, cur_node.left)
                q.insert(0, cur_node.right)

        return ','.join(result_list)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(',')
        if node_list[0] == 'null':
            return None

        root = TreeNode(int(node_list[0]))
        q = [root]
        pointer = 1
        while q:
            l = len(q)
            for i in range(l):
                cur_node = q.pop()
                if cur_node is None:
                    continue

                l_child = node_list[pointer]
                if l_child == 'null':
                    cur_node.left = None
                    q.insert(0, None)
                else:
                    l_node = TreeNode(int(l_child))
                    cur_node.left = l_node
                    q.insert(0, l_node)
                pointer += 1

                r_child = node_list[pointer]
                if r_child == 'null':
                    cur_node.right = None
                    q.insert(0, None)
                else:
                    r_node = TreeNode(int(r_child))
                    cur_node.right = r_node
                    q.insert(0, r_node)
                pointer += 1

                if pointer >= len(node_list):
                    return root

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

#================= Recurison(Pre-order traversal)====================
# Time: O(n)
# Space: O(n)
# Run time: ~200ms

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
