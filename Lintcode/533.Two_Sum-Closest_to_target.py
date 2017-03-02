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
                
