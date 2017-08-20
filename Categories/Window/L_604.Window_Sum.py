"""
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Have you met this question in a real interview? Yes
Example
For array [1,2,7,8,5], moving window size k = 3. 
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
"""

# ============= Sliding window =============
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
