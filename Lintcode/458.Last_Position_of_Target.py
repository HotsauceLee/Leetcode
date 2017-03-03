# ================ Binary Search ================
# Time: O(log(n))
# Space: O(1)
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if not A or not target:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            if A[end] == target:
                return end

            mid = (start + end)//2
            if target >= A[mid]:
                start = mid
            else:
                end = mid - 1

        if A[end] == target:
            return end
        if A[start] == target:
            return start
        return -1
