"""
Find the kth smallest number in at row and column sorted matrix.

Have you met this question in a real interview? Yes
Example
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5
"""

# =========== Heap ==============
# Time: O(k2log(row))
# Space: O(row)
# Category: Kth smallest/biggest with heap
class Node(object):
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col
        
    def __cmp__(self, other):
        return self.val - other.val

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return None
        
        len_row, len_col = len(matrix), len(matrix[0])
        heap = [Node(matrix[row][0], row, 0) for row in xrange(len_row)]
        result = None
        while k >= 1:
            cur_smallest = heapq.heappop(heap)
            result = cur_smallest.val
            k -= 1
            if cur_smallest.col + 1 < len_col:
                heapq.heappush(heap, Node(matrix[cur_smallest.row][cur_smallest.col + 1], cur_smallest.row, cur_smallest.col + 1))

        return result
        
