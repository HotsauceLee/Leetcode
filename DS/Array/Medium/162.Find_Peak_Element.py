# =========== Binary Search ============
# Time: O(log(n))
# Space: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin, end = 0, len(nums) - 1
        while begin < end:
            mid = (begin + end)/2
            # /\
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            # /
            if nums[mid] < nums[mid + 1]:
                begin = mid + 1
            # \ or \/
            else:
                end = mid
                
        return begin
