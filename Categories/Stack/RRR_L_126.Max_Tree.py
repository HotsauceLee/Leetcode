"""
Given an integer array with no duplicates. A max tree building on this array is defined as follow:

The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.

Have you met this question in a real interview? Yes
Example
Given [2, 5, 6, 0, 3, 1], the max tree constructed by this array is:

    6
   / \
  5   3
 /   / \
2   0   1
"""

# ============= Decresing stack ===============
# Time: O(2n)
# Space: O(n)
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        if not A:
            return None
        # for force pop the whole stack at the end
        A.append(float('inf'))
        stack = []
        for a in A:
            new_node = TreeNode(a)
            while stack and new_node.val > stack[-1].val:
                last_node = stack.pop()
                if not stack:
                    new_node.left = last_node
                else:
                    if stack[-1].val > new_node.val:
                        new_node.left = last_node
                    else:
                        stack[-1].right = last_node

            stack.append(new_node)

        return stack[0].left
