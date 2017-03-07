"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 Notice

This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.

Have you met this question in a real interview? Yes
Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
# =============== DP ================
# Time: O(n^2)
# Space: O(n)
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        len_A = len(A)
        if len_A == 1 or A[0] >= len_A - 1:
            return True
        
        dp = [False]*len_A
        dp[0] = True
        for idx in xrange(len_A):
            if dp[-1]:
                return True
            if not dp[idx]:
                continue
            if A[idx] >= len_A - 1 - idx:
                return True
                
            for jump_to in xrange(1, A[idx] + 1):
                dp[idx + jump_to] = True
                
        return False
        """
        #DP
        dp = [False]*len(A)
        dp[0] = True
        for i in xrange(1, len(A)):
            for j in xrange(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
                
        return dp[-1]
        """
