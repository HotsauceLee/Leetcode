"""
There is an integer matrix which has the following features:

The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:

A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.

 Notice

The matrix may contains multiple peeks, find any of them.

Have you met this question in a real interview? Yes
Example
Given a matrix:

[
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])
"""


# ================ log(n)*m ===================
class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        # write your code here
        len_row, len_col = len(A), len(A[0])
        top, bottom = 0, len_row - 1
        while top < bottom:
            row = (top + bottom)/2
            # find col max
            col_max = 0
            for i in xrange(1, len_col):
                if A[row][i] > A[row][col_max]:
                    col_max = i
                    
            # print "[%s, %s]" % (row, col_max)
            if A[row + 1][col_max] > A[row][col_max]:
                # print "going down to [%s, %s]" % (row + 1, col_max)
                top = row
            elif A[row - 1][col_max] > A[row][col_max]:
                # print "going up to [%s, %s]" % (row - 1, col_max)
                bottom = row
            else:
                return [row, col_max]
                
           
# ================= O(n) ===================
# Time: m + n/2 + m/2 + n/4 + m/4 + ..... = 2m + 2n = m + n
# n + n/2 + n/4 + n/8 + .... = 2n
class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        # write your code here
        len_row, len_col = len(A), len(A[0])
        top, bottom, left, right = 0, len_row - 1, 0, len_col - 1
        top_down = True
        while top < bottom and left < right:
            if top_down:
                row = (top + bottom)/2
                # find col max
                col_max = left
                for i in xrange(left + 1, right + 1):
                    if A[row][i] > A[row][col_max]:
                        col_max = i
                        
                if A[row + 1][col_max] > A[row][col_max]:
                    top = row
                elif A[row - 1][col_max] > A[row][col_max]:
                    bottom = row
                else:
                    return [row, col_max]
            else:
                col = (left + right)/2
                # find row max
                row_max = top
                for i in xrange(top + 1, bottom + 1):
                    if A[i][col] > A[row_max][col]:
                        row_max = i
                        
                if A[row_max][col + 1] > A[row_max][col]:
                    left = col
                elif A[row_max][col - 1] > A[row_max][col]:
                    right = col
                else:
                    return [row_max, col]

            top_down = not top_down
            
