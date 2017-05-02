"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.
- You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Have you met this question in a real interview? Yes
Example
Given [4, 1, 5, 10]
Return 270

nums = [4, 1, 5, 10] burst 1, get coins 4 * 1 * 5 = 20
nums = [4, 5, 10]    burst 5, get coins 4 * 5 * 10 = 200 
nums = [4, 10]       burst 4, get coins 1 * 4 * 10 = 40
nums = [10]          burst 10, get coins 1 * 10 * 1 = 10

Total coins 20 + 200 + 40 + 10 = 270
"""

# =============== DP ===============
# Time: O(n^3)
# Space: O(n + n^2 + n^2)
class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins(self, nums):
        # Write your code here
        if not nums:
            return 0
        
        lens = len(nums)
        nums_plus_dummies = [1] + nums + [1]
        
        # build the dp list
        dp = [[-1]*lens for i in xrange(lens)]
            
        self.__dfs(1, lens, dp, nums_plus_dummies)
        return dp[0][-1]
        
    def __dfs(self, left, right, dp, nums):
        if left > right:
            return 0
        if left == right:
            dp[left - 1][right - 1] = nums[left - 1]*nums[left]*nums[left + 1]
            return dp[left - 1][right - 1]
        if dp[left - 1][right - 1] != -1:
            return dp[left - 1][right - 1]
        
        cur_max = float('-inf')
        # when i == right it is the same as dfs(left, right)
        # infinite loop
        for i in xrange(left, right + 1):
            cur_b = nums[left - 1]*nums[i]*nums[right + 1]
            l = self.__dfs(left, i - 1, dp, nums)
            r = self.__dfs(i + 1, right, dp, nums)
            cur_max = max(cur_max, cur_b + l + r)
            
        dp[left - 1][right - 1] = cur_max
        return cur_max
    
    
# =============== Loops DP ==============
# Time: O(n^3)
# Space: O(n + n^2)
class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins(self, nums):
        # Write your code here
        if not nums:
            return 0
        
        lens = len(nums)
        nums_with_walls = [1] + nums + [1]
        
        dp = [[0]*(lens + 2) for i in xrange(lens + 2)]
        
        # window size
        for dist in xrange(1, lens + 1):
            # move window from left to right
            for left in xrange(1, lens - dist + 2):
                right = left + dist - 1
                # iterate inside the window to get the
                # max points of the current window
                for i in xrange(left, right + 1):
                    cur_points = nums_with_walls[left - 1]*nums_with_walls[i]*nums_with_walls[right + 1]
                    dp[left][right] = max(dp[left][right], cur_points + dp[left][i - 1] + dp[i + 1][right])
                    
        return dp[1][lens]
        
        
