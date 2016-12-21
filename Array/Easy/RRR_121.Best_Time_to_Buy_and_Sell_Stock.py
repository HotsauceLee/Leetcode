#============= Kadane's Algorithm===========
# Time: O(n)
# Space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_diff = max_sofar = 0
        for i in xrange(1, len(prices)):
            max_sofar = max(0, max_sofar + prices[i] - prices[i - 1])
            max_diff = max(max_diff, max_sofar)
            
        return max_diff
