"""
Given an circular integer array (the next element of the last element is the first element), find a continuous subarray in it, where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number.

If duplicate answers exist, return any of them.

Have you met this question in a real interview? Yes
Example
Give [3, 1, -100, -3, 4], return [4,1].
"""

# ============= keep both max and min ==============
# Time: O(n)
# Space: O(1)
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySumII(self, A):
        # Write your code here
        if not A:
            return []
            
        min_sum, min_start, min_end = float('inf'), -1, -1
        max_sum, max_start, max_end = float('-inf'), -1, -1
        r_max_start, r_max_end = -1, -1
        r_min_start, r_min_end = -1, -1
        cur_min, cur_max = 1, -1
        all_sum = 0
        for i in xrange(len(A)):
            a = A[i]
            all_sum += a
            if cur_max < 0:
                cur_max = a
                max_start = max_end = i
            else:
                cur_max += a
                max_end = i
                
            if cur_max > max_sum:
                max_sum = cur_max
                r_max_start, r_max_end = max_start, max_end
            
            if cur_min > 0:
                cur_min = a
                min_start = min_end = i
            else:
                cur_min += a
                min_end = i
                
            if cur_min < min_sum:
                min_sum = cur_min
                r_min_start , r_min_end = min_start, min_end
        
        # this is for the case where all are negative
        # return the largest negative.
        if all_sum == min_sum:
            return [r_max_start, r_max_end]
        # this is for max range wraps
        elif all_sum - min_sum > max_sum:
            return [r_min_end + 1, r_min_start - 1]
        # for all other case, max is within range
        return [r_max_start, r_max_end]
            
