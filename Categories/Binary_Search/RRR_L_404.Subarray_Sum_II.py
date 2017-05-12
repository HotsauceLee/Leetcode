"""
Given an integer array, find a subarray where the sum of numbers is in a given interval. Your code should return the number of possible answers. (The element in the array should be positive)

Have you met this question in a real interview? Yes
Example
Given [1,2,3,4] and interval = [1,3], return 4. The possible answers are:

[0, 0]
[0, 1]
[1, 1]
[2, 2]
"""

# ============== BS ================
# Time: O(nlogn)
# Space: O(1)
class Solution:
    # @param {int[]} A an integer array
    # @param {int} start an integer
    # @param {int} end an integer
    # @return {int} the number of possible answer
    def subarraySumII(self, A, start, end):
        # Write your code here
        if not A or start > end:
            return 0
            
        for i in xrange(1, len(A)):
            A[i] += A[i - 1]

        A.sort()
        result = 0
        for a in A:
            if start <= a <= end:
                result += 1
            small = a - end
            big = a - start
            # start <= sums[i] - sums[j - 1] <= end
            # => sums[i] - start >= sums[j - 1] >= sums[i] - end
            # => (num of sums[j - 1] < big + 1(<= big)) - (num of sums[j - 1] <= small)
            result += self.__bs(A, big + 1) - self.__bs(A, small)

        return result
            
    def __bs(self, A, value):
        lens = len(A)
        if A[-1] < value:
            return lens
            
        begin, end = 0, lens - 1
        while begin + 1 < end:
            mid = (begin + end)/2
            if A[mid] >= value:
                end = mid - 1
            else:
                begin = mid

        if end < 0 or (A[end] >= value and A[begin] >= value):
            return 0
        if A[end] < value:
            return end + 1
            
        return begin + 1
