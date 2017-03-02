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
            
