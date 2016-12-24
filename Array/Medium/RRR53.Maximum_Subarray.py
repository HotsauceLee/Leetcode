#================ Kadane's algorithm =============
# Time: O(n)
# Space: O(1)
# Idea:
#    algorithm that operates on arrays: it starts at
#    the left end (element A[1]) and scans through to
#    the right end (element A[n]), keeping track of 
#    the maximum sum subvector seen so far. The maximum
#    is initially A[0]. Suppose we've solved the problem
#    for A[1 .. i - 1]; how can we extend that to A[1 .. i]?
#    The maximum sum in the first I elements is either 
#    the maximum sum in the first i - 1 elements (which 
#    we'll call MaxSoFar), or it is that of a subvector 
#    that ends in position i (which we'll call MaxEndingHere).
#    MaxEndingHere is either A[i] plus the previous MaxEndingHere,
#    or just A[i], whichever is larger.
# array elements must be mix of positive and negative numbers, or
# the answer will always be the whole array.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = float('-inf')
        for n in nums:
            max_ending_here = max(max_ending_here + n, n)
            max_so_far = max(max_so_far, max_ending_here)
            
        return max_so_far
# ================== DP ===================
# Timee: O(n)
# Space: O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        max_sub = dp[0]
        
        for i in xrange(1, len(nums)):
            dp[i] = nums[i] + dp[i - 1] if dp[i - 1] > 0 else nums[i]
            max_sub = max(max_sub, dp[i])
            
        return max_sub
# ================ Divide and Concur ==============
