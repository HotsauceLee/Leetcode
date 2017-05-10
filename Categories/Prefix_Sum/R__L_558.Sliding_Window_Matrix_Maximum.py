"""
Given an array of n * m matrix, and a moving matrix window (size k * k), move the window from top left to botton right at each iteration, find the maximum sum inside the window at each moving.
Return 0 if the answer does not exist.

Have you met this question in a real interview? Yes
Example
For matrix

[
  [1, 5, 3],
  [3, 2, 1],
  [4, 1, 9],
]
The moving window size k = 2. 
return 13.

At first the window is at the start of the array like this

[
  [|1, 5|, 3],
  [|3, 2|, 1],
  [4, 1, 9],
]
,get the sum 11;
then the window move one step forward.

[
  [1, |5, 3|],
  [3, |2, 1|],
  [4, 1, 9],
]
,get the sum 11;
then the window move one step forward again.

[
  [1, 5, 3],
  [|3, 2|, 1],
  [|4, 1|, 9],
]
,get the sum 10;
then the window move one step forward again.

[
  [1, 5, 3],
  [3, |2, 1|],
  [4, |1, 9|],
]
,get the sum 13;
SO finally, get the maximum from all the sum which is 13.
"""

# ============== Prefix sum =============
# Time: O((m*n)^2)
# Space: O(m*n)
class Solution:
    # @param {int[][]} matrix an integer array of n * m matrix
    # @param {int} k an integer
    # @return {int} the maximum number
    def maxSlidingMatrix(self, matrix, k):
        # Write your code here
        if not matrix or not matrix[0]:
            return 0
        
        len_row, len_col = len(matrix), len(matrix[0])
        if k > len_row or k > len_col:
            return 0
        if k == len_row and k == len_col:
            return sum(map(lambda x: sum(x), matrix))
        
        # O(m*n)
        sums = [[0]*(len_col + 1) for i in xrange(len_row + 1)]
        for row in xrange(1, len_row + 1):
            for col in xrange(1, len_col + 1):
                sums[row][col] = sums[row - 1][col] + \
                                 sums[row][col - 1] - \
                                 sums[row - 1][col - 1] + \
                                 matrix[row - 1][col - 1]
        
        # O(n*m)     
        max_sum = float('-inf')
        for row in xrange(k - 1, len_row):
            for col in xrange(k - 1, len_col):
                cur_sum = sums[row + 1][col + 1] - \
                          sums[row + 1 - k][col + 1] - \
                          sums[row + 1][col + 1 - k] + \
                          sums[row + 1 - k][col + 1 - k]
                          
                max_sum = max(max_sum, cur_sum)
                
        return max_sum
