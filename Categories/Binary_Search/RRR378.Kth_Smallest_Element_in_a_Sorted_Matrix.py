# =========== Binary Search ============
# Time: m*n*log(m*n)
# Space: O(1)
# Trap: mid might not in matrix
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return None
            
        if k == 1:
            return matrix[0][0]
        len_row, len_col = len(matrix), len(matrix[0])
        if k == len_row*len_col:
            return matrix[-1][-1]
            
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi)/2
            # if count(n <= mid) == k, then mid could be the result
            # but matrix might not contain mid, so we have to keep
            # moving to find the smallest that =count(n <= mid) == k.
            # For instance: 14 in [[1,5,9],[10,11,13],[12,13,15]]
            smaller_or_equals_than_mid = 0
            for row in xrange(len_row):
                col = 0
                count = 0
                while col < len_col and matrix[row][col] <= mid:
                    col += 1
                    smaller_or_equals_than_mid += 1
                    
            if smaller_or_equals_than_mid < k:
                lo = mid + 1
            else:
                hi = mid
                
        return lo
