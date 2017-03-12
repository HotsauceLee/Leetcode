#============= Kadane's Algorithm===========
# Time: O(n)
# Space: O(1)
# Idea:
#    a b c d e
#    (b-a) + (c-b) + (d-c) + (e-d) = e - a
# Same as maximum subarray problem, but find the largest sequence of differences.
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

# ========== Keep track of min element and update max diff ======
# Time: O(n)
# Space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_so_far = float('inf')
        max_diff = 0
        for n in prices:
            if n < min_so_far:
                min_so_far = n
                continue
            
            max_diff = max(max_diff, n - min_so_far)
            
        return max_diff
