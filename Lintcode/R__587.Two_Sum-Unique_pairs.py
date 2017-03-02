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
