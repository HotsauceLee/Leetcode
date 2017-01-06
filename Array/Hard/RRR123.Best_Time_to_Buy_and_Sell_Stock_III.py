# ========== Max(i) = Max(0:i) + Max(i+1:) =========
# Time: O(3n)
# Space: O(2n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        
        left_to_right = [0]*len(prices)
        right_to_left = [0]*len(prices)
        left, min_left, m_left = 0, float('inf'), 0
        for left in xrange(len(prices)):
            min_left = min(min_left, prices[left])
            m_left = max(m_left, prices[left] - min_left)
            left_to_right[left] = m_left
            
        right, max_right, m_right = len(prices) - 1, float('-inf'), 0
        for right in xrange(len(prices) - 1, -1, -1):
            max_right = max(max_right, prices[right])
            m_right = max(m_right, max_right - prices[right])
            right_to_left[right] = m_right
            
        result = 0
        for i in xrange(len(prices)):
            result = max(result, left_to_right[i] + right_to_left[i])
            
        return result
        
# ========== Same with one less loop ==============
# Time: O(2n)
# Space: O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        
        right_to_left = [0]*len(prices)
        right, max_right, m_right = len(prices) - 1, float('-inf'), 0
        for right in xrange(len(prices) - 1, -1, -1):
            max_right = max(max_right, prices[right])
            m_right = max(m_right, max_right - prices[right])
            right_to_left[right] = m_right
            
        min_left, m_left, result = float('inf'), 0, 0
        for i in xrange(len(prices)):
            min_left = min(min_left, prices[i])
            m_left = max(m_left, prices[i] - min_left)
            result = max(result, m_left + right_to_left[i])
            
        return result  

# ======TODO =========
"""
The thinking is simple and is inspired by the best solution from Single Number II (I read through the discussion after I use DP).
Assume we only have 0 money at first;
4 Variables to maintain some interested 'ceilings' so far:
The maximum of if we've just buy 1st stock, if we've just sold 1nd stock, if we've just buy 2nd stock, if we've just sold 2nd stock.
Very simple code too and work well. I have to say the logic is simple than those in Single Number II.

public class Solution {
    public int maxProfit(int[] prices) {
        int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE;
        int release1 = 0, release2 = 0;
        for(int i:prices){                              // Assume we only have 0 money at first
            release2 = Math.max(release2, hold2+i);     // The maximum if we've just sold 2nd stock so far.
            hold2    = Math.max(hold2,    release1-i);  // The maximum if we've just buy  2nd stock so far.
            release1 = Math.max(release1, hold1+i);     // The maximum if we've just sold 1nd stock so far.
            hold1    = Math.max(hold1,    -i);          // The maximum if we've just buy  1st stock so far. 
        }
        return release2; ///Since release1 is initiated as 0, so release2 will always higher than release1.
    }
}
"""
