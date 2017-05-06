"""
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

 Notice

You can not divide any item into small pieces.

Have you met this question in a real interview? Yes
Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.
"""

# ================ DP =================
# Time: O(n*m)
# Space: O(2m)
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        if not A:
            return 0
          
        # dp - prev row
        dp = [False]*(m + 1)
        dp[0] = True
        cur_row = []
        # i - (not)take the ith item
        # S - backpack vol
        result = float('-inf')
        for i in xrange(1, len(A) + 1):
            for S in xrange(m + 1):
                # dp[i - 1][S]            => not take i
                # dp[i - 1][S - A[i - 1]] => take i
                take = dp[S - A[i - 1]] if S - A[i - 1] >= 0 else False
                cur_vol = dp[S] or take
                cur_row.append(cur_vol)
                if i == len(A) and cur_vol:
                    result = max(result, S)
            dp = cur_row
            cur_row = []
                    
        return result
