"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.


After the rain, water are trapped between the blocks. The total volume of water trapped is 4.
"""

# =========== Outside to inside =============
# Time: O(m*n*log(2m + 2n)) m, n - len_row, len_col
# Space: O(2m + 2n)
class Node(object):
    def __init__(self, r, c, val):
        self.r = r
        self.c = c
        self.val = val
        
    def __cmp__(self, other):
        return self.val - other.val

import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        len_row, len_col = len(heightMap), len(heightMap[0])
        if len_row <= 2 or len_col <= 2:
            return 0

        delta_x = [0, 0, 1, -1]
        delta_y = [1, -1, 0, 0]
        visited = [[False]*len_col for i in xrange(len_row)]
        
        heap = []
        top, bot = 0, len_row - 1
        for i in xrange(len_col):
            heapq.heappush(heap, Node(top, i, heightMap[top][i]))
            heapq.heappush(heap, Node(bot, i, heightMap[bot][i]))
            visited[top][i] = True
            visited[bot][i] = True
            
        left, right = 0, len_col - 1
        for i in xrange(len_row):
            heapq.heappush(heap, Node(i, left, heightMap[i][left]))
            heapq.heappush(heap, Node(i, right, heightMap[i][right]))
            visited[i][left] = True
            visited[i][right] = True
        
        def inbound(r, c):
            return 0 <= r < len_row and 0 <= c < len_col

        result = 0
        while heap:
            cur = heapq.heappop(heap)
            for i in xrange(4):
                next_row = cur.r + delta_x[i]
                next_col = cur.c + delta_y[i]
                if inbound(next_row, next_col) and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    # This is important. This ensures that the wall will go inside in every step.
                    # which is the same as maintaining the max left/right as in 1d trapping water.
                    # the heap will eventually gone empty.
                    heapq.heappush(heap, Node(next_row, next_col, max(cur.val, heightMap[next_row][next_col])))
                    result += max(0, cur.val - heightMap[next_row][next_col])

        return result
