# =========== DP ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
            
        min_result = float('inf')
        for r in xrange(1, len(triangle)):
            for c in xrange(len(triangle[r])):
                if c == 0:
                    triangle[r][c] += triangle[r - 1][c]
                elif c == len(triangle[r]) - 1:
                    triangle[r][c] += triangle[r - 1][c - 1]
                else:
                    triangle[r][c] += min(triangle[r - 1][c], triangle[r - 1][c - 1])
                    
                if r == len(triangle) - 1:
                    min_result = min(min_result, triangle[r][c])
                    
        return min_result if min_result != float('inf') else triangle[0][0]
