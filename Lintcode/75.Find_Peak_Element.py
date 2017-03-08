"""
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peek if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

 Notice

The array may contains multiple peeks, find any of them.

Have you met this question in a real interview? Yes
Example
Given [1, 2, 1, 3, 4, 5, 7, 6]

Return index 1 (which is number 2) or 6 (which is number 7)
"""
# ============== Binary Search ===============
# Time: O(log(n))
# Space: O(1)
# 1. middle of uphill: n[mid] < n[mid + 1]
# 2. middle of downhill: n[mid - 1] > n[mid]
# 3. bottom: n[mid] < n [mid -1] and n[mid + 1]
# 4. peak: n[mid] > n [mid -1] and n[mid + 1]
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        begin, end = 1, len(A) - 2
        while begin + 1 < end:
            mid = (begin + end)/2
            
            if A[mid] < A[mid + 1]:
                begin = mid
            elif A[mid - 1] > A[mid]:
                end = mid
            else:
                return mid
                
        if A[begin] > A[end]:
            return begin
            
        return end
