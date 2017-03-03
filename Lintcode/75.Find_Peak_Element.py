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
