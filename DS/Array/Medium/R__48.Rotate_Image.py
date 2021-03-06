# ========== Brutal Force ===========
# Time: O(2*N^2)
# Space: O(n^2)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # [[0]*n]*n will initialize an array with the same row objects.
        lens = len(matrix)
        columns = [0]*lens
        copy = [columns[:] for i in xrange(lens)]
        for r in xrange(lens):
            for c in xrange(lens):
                copy[r][c] = matrix[lens - 1 - c][r]
                
        for r in xrange(lens):
            for c in xrange(lens):
                matrix[r][c] = copy[r][c]
                
# ============ Python swap variable values ============
# Time: (n-2*0-1)+(n-2*1-1)+(n-2*2-1)+....+(n-2*(n/2)-1)
# Space: O(1)
# Idea: Get the 4 edges of current cube and use relative positions.
class Solution:
    def rotate(self, A):
        n = len(A)
        for i in xrange(n/2):
            lens = len(A) - i*2
            top, bottom, left, right = i, n-1-i, i, n-1-i
            for j in xrange(lens-1):
                A[top][left+j],    A[top+j][right], A[bottom][right-j], A[bottom-j][left] = \
                A[bottom-j][left], A[top][left+j],  A[top+j][right],    A[bottom][right-j]
                
# =========== Swap in place ==============
# Time: O(n/2 + n^2)
# Space: O(1)
"""
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def reverse(input):
            begin, end = 0, len(input) - 1
            while begin < end:
                input[begin], input[end] = input[end], input[begin]
                begin += 1
                end -= 1
                
        reverse(matrix)
        for r in xrange(len(matrix)):
            for c in xrange(r + 1, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
# =========== Zip ==============
# Time: matrix[::-1] - n + zip - n + matrix[:] = zip - n => O(3n)
# Space: O(n^2)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])
