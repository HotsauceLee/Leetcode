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
