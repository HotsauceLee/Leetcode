"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

 Notice

If there are multiple solutions, return any subset is fine.

Have you met this question in a real interview? Yes
Example
Given nums = [1,2,3], return [1,2] or [1,3]

Given nums = [1,2,4,8], return [1,2,4,8]
"""
# ============ DP =============
# Time: O(n^2)
# Space: O(2n)
class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset 
    def largestDivisibleSubset(self, nums):
        # Write your code here
        if not nums:
            return []
    
        nums.sort()
        nums_lens = len(nums)
        max_so_far = [0]*nums_lens
        pre_pos = [0]*nums_lens
        max_num = 0 
        max_i = 0
        for i in xrange(nums_lens):
            max_so_far[i] = 1 
            pre_pos[i] = i 
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    max_so_far[i] = max_so_far[j] + 1 
                    pre_pos[i] = j 
            if max_so_far[i] > max_num:
                max_num = max_so_far[i]
                max_i = i

        result = collections.deque()
        result.appendleft(nums[max_i])
        while max_i != pre_pos[max_i]:
            max_i = pre_pos[max_i]
            result.appendleft(nums[max_i])

        return list(result)
