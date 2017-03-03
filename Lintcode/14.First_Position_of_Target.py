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
            
