# =============== Binary Search =============
# Time: O(log(n))
# Space: O(1)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return None

        begin, end = 0, len(nums) - 1 
        while begin + 1 < end:
            mid = (begin + end)/2

            if nums[mid] == target:
                return mid 

            if nums[mid] > target:
                end = mid 
            else:
                begin = mid 

        if nums[begin] == target:
            return begin
        if nums[end] == target:
            return end 
        if target < nums[begin]:
            return begin
        if target > nums[end]:
            return end + 1 

        return end 
