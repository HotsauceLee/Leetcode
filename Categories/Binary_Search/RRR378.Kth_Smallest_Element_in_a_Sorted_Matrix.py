"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n^2.
"""

# =========== Binary Search ============
# Time: n*log(n)*log(lo-hi)
# Space: O(1)
# Trap: how do we guarantee the result is in matrix?
"""
https://discuss.leetcode.com/topic/52865/my-solution-using-binary-search-in-c/32

if smaller_or_equals_than_mid < k:
    lo = mid + 1
else:
    hi = mid
    
1. When smaller_or_equals_than_mid < k:
smaller_or_equals_than_mid elements could be all < mid or all <= mid
  if all < mid, mid not in matrix, so do the elements < mid, lo = mid + 1
  if all <= mid, mid could not be the answer, lo = mid + 1

2. When smaller_or_equals_than_mid >= k:
  a. when smaller_or_equals_than_mid == k
    smaller_or_equals_than_mid elements could be all < mid or all <= mid
    if all < mid, mid not in matrix, answer must < mid, hi = mid
    e.g. [[1,5,9],[10,11,13],[12,13,15]] mid = 14
    if all <= mid, mid is the answer, lo will lean toward it later, hi = mid
    e.g. [[1,5,9],[10,11,13],[12,13,15]] mid = 13
  b. when smaller_or_equals_than_mid > k:
    answer must < mid, no matter mid in matrix or not, hi = mid
    
In conclusion, when smaller_or_equals_than_mid >= k, answer <= mid, so
hi = mid instead of hi = mid - 1
"""
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
        # log(lo-hi)
        while lo < hi:
            mid = (lo + hi)/2
            # if count(n <= mid) == k, then mid could be the result
            # but matrix might not contain mid, so we have to keep
            # moving to find the smallest that =count(n <= mid) == k.
            # For instance: 14 in [[1,5,9],[10,11,13],[12,13,15]]
            smaller_or_equals_than_mid = 0
            # O(n)
            for row in xrange(len_row):
                col = 0
                count = 0
                # log(len_col), in this problem len_col == len_row == n
                while col < len_col and matrix[row][col] <= mid:
                    col += 1
                    smaller_or_equals_than_mid += 1
                    
            if smaller_or_equals_than_mid < k:
                lo = mid + 1
            else:
                hi = mid
                
        return lo
