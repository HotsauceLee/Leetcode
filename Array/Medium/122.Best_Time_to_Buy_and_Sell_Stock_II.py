# ======== add to result when diff > 0 ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] - prices[i-1] > 0: max_profit += prices[i] - prices[i-1]
            
        return max_profit
        
# ========== Python one liner ==============
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([n for n in map(lambda x, y: y -x, [float('inf')]+prices, prices+[-1]) if n > 0])
