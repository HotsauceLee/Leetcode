"""
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Have you met this question in a real interview? Yes
Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.
"""
# ============= Binary Search =============
# Time: O(log(n))
# Space: O(1)
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if not nums or not target: return -1
        
        begin, end = 0, len(nums) - 1
        while begin + 1 < end:
            mid = (begin + end)/2
            mid_value = nums[mid]
            
            if mid_value >= target:
                end = mid
            else:
                begin = mid
                
        if nums[begin] == target:
            return begin
        if nums[end] == target:
            return end
        
        return -1
            
