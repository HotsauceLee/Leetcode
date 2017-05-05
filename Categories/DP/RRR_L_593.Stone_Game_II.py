"""
There is a stone game.At the beginning of the game the player picks n piles of stones in a circle.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

Have you met this question in a real interview? Yes
Example
For [1, 4, 4, 1], in the best solution, the total score is 18:

1. Merge second and third piles => [2, 4, 4], score +2
2. Merge the first two piles => [6, 4]，score +6
3. Merge the last two piles => [10], score +10
Other two examples:
[1, 1, 1, 1] return 8
[4, 4, 5, 9] return 43
"""

# ============== DP =============
# Time: O(n^3 + n)
# Space: O(2n + n^2)
class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame2(self, A):
        # Write your code here
        if not A:
            return 0
        lens = len(A)
        if lens == 1:
            return 0

        sums = [0]*(lens*2)
        for i in xrange(1, len(sums)):
            sums[i] = sums[i - 1] + A[(i - 1)%lens]
            
        dp = [[0]*(lens*2 - 1) for i in xrange(lens*2 - 1)]
        for window in xrange(2, lens + 1):
            for left in xrange(0, (lens*2 - 1) - window):
                right = left + window - 1
                cur_sum = sums[right + 1] - sums[left]
                cur_min = float('inf')
                for i in xrange(left, right):
                    cur_min = min(cur_min, dp[left][i] + dp[i + 1][right])
                dp[left][right] = cur_min + cur_sum
        
        result = float('inf')
        for i in xrange(0, lens - 1):
            result = min(result, dp[i][i + lens - 1])
            
        return result
