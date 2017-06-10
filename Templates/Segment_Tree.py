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
