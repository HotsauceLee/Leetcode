# ========== Sort + lo&hi pointers ===========
# Time: O(nlog(n))
# Space: O(1)
class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        # Write your code here
        if not nums:
            return 0
        
        nums.sort()
        lo, hi, result = 0, len(nums) - 1, 0
        while lo < hi:
            if nums[lo] + nums[hi] > target:
                result += hi - lo
                hi -= 1
            else:
                lo += 1
                
        return result
