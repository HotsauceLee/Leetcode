"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""

# ================= ST =================
class SegmentTreeNode(object):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.left = None
        self.right = None
        self.s = 0

class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(self.nums, 0, len(nums) - 1)
    
    # Time: O(n). Space: O(n)
    def build(self, nums, begin, end):
        if begin > end:
            return None
        
        cur_node = SegmentTreeNode(begin, end)
        if begin == end:
            cur_node.s = nums[begin]
        else:
            mid = (begin + end)/2
            cur_node.left = self.build(nums, begin, mid)
            cur_node.right = self.build(nums, mid + 1, end)
            cur_node.s = cur_node.left.s + cur_node.right.s
        
        return cur_node
    
    # O(log(n))
    def update(self, i, val):
        if i < 0 or i >= len(self.nums):
            return
        
        self.nums[i] = val
        self.__update(i, val, self.root)
        
    def __update(self, i, val, node):
        begin, end = node.begin, node.end
        if begin == end:
            node.s = val
        else:
            mid = (begin + end)/2
            if i <= mid:
                self.__update(i, val, node.left)
            else:
                self.__update(i, val, node.right)
                
            node.s = node.left.s + node.right.s
    
    # O(log(n))
    def query(self, i, j):
        if i > j or i < 0 or j >= len(self.nums):
            return None
            
        if i == j:
            return self.nums[i]
            
        return self.__query(self.root, i, j)
        
    def __query(self, node, i, j):
        begin, end = node.begin, node.end
        if i == begin and j == end:
            return node.s

        mid = (begin + end)/2
        if j <= mid:
            return self.__query(node.left, i, j)
        elif i > mid:
            return self.__query(node.right, i, j)
        else:
            left_sum = self.__query(node.left, i, mid)
            right_sum = self.__query(node.right, mid + 1, j)
            return left_sum + right_sum
        

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.st = SegmentTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.st.update(i, val)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.st.query(i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
