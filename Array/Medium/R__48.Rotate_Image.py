# ========== Brutal Force ===========
# Time: O(2*N^2)
# Space: O(n)
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
                
# =========== Swap in place ==============
# Time: O(n/2 + n^2)
# Space: O(1)
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
