# =========== Add next substract last ===========
# Time: O(n)
# Space: O(1)
class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        if not nums or len(nums) < k or k < 0:
            return []
            
        result = [sum(nums[:k])]
        for i in xrange(len(nums) - k):
            result.append(result[-1] - nums[i] + nums[i + k])
            
        return result
