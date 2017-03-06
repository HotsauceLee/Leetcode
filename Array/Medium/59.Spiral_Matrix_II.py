# ============ Magic ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        if n == 1:
            return [[1]]
            
        result = [[0]*n for i in xrange(n)]
        cur_num = 1
        min_row = min_col = 0
        max_row = max_col = n - 1
        while min_row <= max_row and min_col <= max_col:
            # Go right
            for c in xrange(min_col, max_col + 1):
                result[min_row][c] = cur_num
                cur_num += 1
            min_row += 1
            
            # Go down
            for d in xrange(min_row, max_row + 1):
                result[d][max_col] = cur_num
                cur_num += 1
            max_col -= 1
            
            # Go left
            for l in xrange(max_col, min_col - 1, -1):
                result[max_row][l] = cur_num
                cur_num += 1
            max_row -= 1
                
            # Go up
            for u in xrange(max_row, min_row - 1, -1):
                result[u][min_col] = cur_num
                cur_num += 1
            min_col += 1
                
        return result
                
                
                
"""
Solution 1: Build it inside-out - 44 ms, 5 lines

Start with the empty matrix, add the numbers in reverse order until we added the number 1. Always rotate the matrix clockwise and add a top row:

    ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                     |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                         |8 7|      |7 6 5|
The code:

def generateMatrix(self, n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A
While this isn't O(n^2), it's actually quite fast, presumably due to me not doing much in Python but relying on zip and range and + being fast. I got it accepted in 44 ms, matching the fastest time for recent Python submissions (according to the submission detail page).

Solution 2: Ugly inside-out - 48 ms, 4 lines

Same as solution 1, but without helper variables. Saves a line, but makes it ugly. Also, because I access A[0][0], I had to handle the n=0 case differently.

def generateMatrix(self, n):
    A = [[n*n]]
    while A[0][0] > 1:
        A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
    return A * (n>0)
Solution 3: Walk the spiral - 52 ms, 9 lines

Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n. Make a right turn when the cell ahead is already non-zero.

def generateMatrix(self, n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A
"""
