"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""

# =============== traversal with stop ==============
# Time: O(m*n)
# Space: O(1)
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        len_row, len_col = len(matrix), len(matrix[0])
        result = []
        delta, d = ((-1 , 1), (1, -1)), 0
        row = col = 0
        while row < len_row and col < len_col:
            # print "before: %s, %s" % (row, col)
            result.append(matrix[row][col])
            row += delta[d][0]
            col += delta[d][1]
            # print "after: %s, %s" % (row, col)
            # print "\n"
            
            # too down and too right must be first
            # 'cause too down and too left could happen at the same time
            # so does too right and too up. we want to treat them as
            # too down and too too right when that happens.
            
            # too down
            if row >= len_row:
                row = len_row - 1
                col += 2
                d = 1 - d
            # too right
            if col >= len_col:
                col = len_col - 1
                row += 2
                d = 1 - d
            # too up
            if row < 0:
                row = 0
                d = 1 - d
            # too left
            if col < 0:
                col = 0
                d = 1 - d
            
                
        return result
                
