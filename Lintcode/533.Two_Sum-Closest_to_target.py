"""
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.

Have you met this question in a real interview? Yes
Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).
"""
# =========== Left and right pointers ==========
# Time: O(n)
# Space: O(1)
class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        if not nums or len(nums) < 2:
            return 0
        
        nums.sort()
        begin, end, result = 0, len(nums) - 1, float('inf')
        while begin < end:
            cur_sum = nums[begin] + nums[end]
            if cur_sum == target:
                return 0
            
            result = min(abs(cur_sum - target), result)
            if cur_sum > target:
                end -= 1
            else:
                begin += 1
                
        return result
                
