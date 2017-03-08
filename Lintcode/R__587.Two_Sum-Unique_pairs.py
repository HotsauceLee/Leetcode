"""
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Have you met this question in a real interview? Yes
Example
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
"""
# ============ Left and right pointers ==============
# Time: O(n)
# Space: O(1)
class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here
        if not nums or len(nums) < 2:
            return 0
         
        nums.sort() 
        begin, end, result = 0, len(nums) - 1, 0
        while begin < end:
            cur_sum = nums[begin] + nums[end]
            if cur_sum == target:
                    result += 1

            if cur_sum >= target:
                while begin < end and nums[end - 1] == nums[end]:
                    end -= 1
                end -= 1
            else:
                while begin < end and nums[begin + 1] == nums[begin]:
                    begin += 1
                begin += 1
                
        return result
