"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

# ========== two binary searches =============
# Time: O(2log(n))
# Space: O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
            
        # find end
        begin, end = 0, len(nums) - 1
        while begin < end:
            mid = (begin + end)/2
            
            if nums[mid] <= target:
                begin = mid + 1
            else:
                end = mid
        
        tail = -1
        if begin > 0 and nums[begin - 1] == target:
            tail = begin - 1
        if nums[begin] == target:
            tail = begin
        if tail == -1:
            return [-1, -1]

        # find begin
        begin, end = 0, len(nums) - 1
        while begin + 1 < end:
            mid = (begin + end)/2
            
            if nums[mid] < target:
                begin = mid
            else:
                end = mid
                
        head = -1
        if nums[end] == target:
            head = end
        if nums[begin] == target:
            head = begin
            
        return [head, tail]


# =============== better ===================

# ============= one algo, target + 1 ===============
