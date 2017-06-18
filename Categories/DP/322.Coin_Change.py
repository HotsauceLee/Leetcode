"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

# ============= DP ===============
# Time: O(amount*len(coins))
# Space: O(amount)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount < 0:
            return -1
        if amount == 0:
            return 0
            
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0
        for i in xrange(1, len(dp)):
            for j in coins:
                remain = float('inf') if i - j < 0 else dp[i - j]
                dp[i] = min(dp[i], remain + 1)
                
        return dp[-1] if dp[-1] < float('inf') else -1
