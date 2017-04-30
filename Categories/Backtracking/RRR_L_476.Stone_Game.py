"""
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

Have you met this question in a real interview? Yes
Example
For [4, 1, 1, 4], in the best solution, the total score is 18:

1. Merge second and third piles => [4, 2, 4], score +2
2. Merge the first two piles => [6, 4]，score +6
3. Merge the last two piles => [10], score +10
Other two examples:
[1, 1, 1, 1] return 8
[4, 4, 5, 9] return 43
"""

# ============ Memory Search ============
# Time: O(n^2)
# Space: O(n + n^2 + n^2)
class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        # Write your code here
        if not A:
            return 0
        
        lens = len(A)
        # build the sums list
        sums = [0]*(lens + 1)
        for i in xrange(1, lens + 1):
            sums[i] = sums[i - 1] + A[i - 1]
        
        # build the dp list
        dp = [[0]*lens for i in xrange(lens)]
            
        return self.__dfs(0, lens - 1, dp, sums)
        
    def __dfs(self, left, right, dp, sums):
        if left > right or left == right:
            return 0

        cur_sum = sums[right + 1] - sums[left]
        if left == right + 1 or right == left + 1:
            return cur_sum
        if dp[left][right] != 0:
            return dp[left][right]
            
        cur_min = float('inf')
        for i in xrange(left, right):
            l = self.__dfs(left, i, dp, sums)
            r = self.__dfs(i + 1, right, dp, sums)
            cur_min = min(cur_min, l + r)

        dp[left][right] = cur_min + cur_sum
        return cur_min + cur_sum
