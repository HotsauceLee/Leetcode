"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

# ============= Build result while looping A and B ===============
# Time: O(A_row*A_col*B_col)
# Space: O(1)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A[0] and not B:
            return []
            
        result_row_len = len(A)
        result_col_len = len(B[0])
        result = [[0]*result_col_len for i in xrange(result_row_len)]
        
        for A_row in xrange(result_row_len):
            for A_col in xrange(len(A[0])):
                if A[A_row][A_col] != 0:
                    for B_col in xrange(result_col_len):
                        result[A_row][B_col] += A[A_row][A_col]*B[A_col][B_col]
                        
        return result
            
            
        
