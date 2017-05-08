"""
Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number. (If their are duplicate answer, return anyone)

Have you met this question in a real interview? Yes
Example
Give [-3, 1, 3, -3, 4], return [1,4].
"""

# ============= tard ===========
# Time: O(n)
# Space: O(1)
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here
        if not A:
            return []
            
        cur_sum, max_sum = -1, float('-inf')
        start = end = -1
        result = [start, end]
        for i in xrange(len(A)):
            a = A[i]
            if cur_sum < 0:
                cur_sum = a
                start = end = i
            else:
                cur_sum += a
                end = i
                
            if cur_sum > max_sum:
                result = [start, end]
                max_sum = cur_sum

        return result
