"""
Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).

Have you met this question in a real interview? Yes
Example
Given a matrix:

[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25
"""

# ============= Memorized Backtracking ===========
# Time: ?
# Space: O(m*n)
class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        # Write your code here
        if not A or not A[0]:
            return 0
            
        self.len_row, self.len_col = len(A), len(A[0])
        self.delta_row = [0, 0, 1, -1]
        self.delta_col = [1, -1, 0, 0]
        
        self.dp = [[0]*self.len_col for i in xrange(self.len_row)]
        
        result = float('-inf')
        for row in xrange(self.len_row):
            for col in xrange(self.len_col):
                result = max(result, self.__dfs(row, col, A))
                
        return result
        
    def __dfs(self, row, col, A):
        if self.dp[row][col] < 0:
            return self.dp[row][col]*-1
            
        max_here = 1
        for i in xrange(len(self.delta_row)):
            next_row = row + self.delta_row[i]
            next_col = col + self.delta_col[i]
            # the next one will be smaller than this one, so it will never come back
            if self.__within_bound(next_row, next_col) and A[row][col] > A[next_row][next_col]:
                max_here = max(max_here, self.__dfs(next_row, next_col, A) + 1)
                
        self.dp[row][col] = max_here*-1
        return max_here
        
    def __within_bound(self, row, col):
        return 0 <= row < self.len_row and 0 <= col < self.len_col
