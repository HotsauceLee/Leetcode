"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

 Notice

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Have you met this question in a real interview? Yes
Example
Given the following triangle:

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""
# ========== DP ============
# Time: O(N = all nodes)
# Space: O(1)
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        
        min_result = float('inf')
        for level in xrange(1, len(triangle)):
            cur_level = triangle[level]
            cur_len = len(cur_level)
            for col in xrange(cur_len):
                if col > 0 and col < cur_len - 1:
                    triangle[level][col] += min(triangle[level - 1][col - 1], triangle[level - 1][col])
                if col == 0:
                    triangle[level][col] += triangle[level - 1][col]
                if col == cur_len - 1:
                    triangle[level][col] += triangle[level - 1][col - 1]
                    
                if level == len(triangle) - 1:
                    min_result = min(min_result, triangle[level][col])
                    
        
        return min_result
            
