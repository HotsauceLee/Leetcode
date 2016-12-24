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
# Time: O(nlog(n))
# Space: O(log(n))
# Idea: 
"""
find mid, recursively get left max and right max, then
get the max across mid, return the largest among these
three. 

In this code, left max already includes mid, but it
doesn't matter because if left max doesn't include
mid, then left max will be larger than max across mid.
if left max includes mid, max across mid will include
left max and the largest one will depends on right max,
which is still the right result.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums, left, right):
            if left == right: return nums[left]
            
            mid = (right + left)/2
            leftmax = helper(nums, left, mid)
            rightmax = helper(nums, mid + 1, right)
            mid_to_left_max = nums[mid]
            mid_to_right_sum = nums[mid + 1]
            
            tmp = 0
            mid_to_left = mid
            while mid_to_left >= left:
                tmp += nums[mid_to_left]
                mid_to_left_max = max(mid_to_left_max, tmp)
                mid_to_left -= 1
                
            tmp = 0
            mid_to_right = mid + 1
            while mid_to_right <= right:
                tmp += nums[mid_to_right]
                mid_to_right_sum = max(mid_to_right_sum, tmp)
                mid_to_right += 1
                
            max_include_mid = mid_to_left_max + mid_to_right_sum
            return max(max(leftmax, rightmax), max_include_mid)
            
        lens = len(nums)
        return 0 if lens == 0 else helper(nums, 0, lens - 1)
