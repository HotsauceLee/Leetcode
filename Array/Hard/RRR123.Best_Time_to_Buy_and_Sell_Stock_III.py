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

# ====== DP - what if buy/sell first one now and buy/sell second one now=========
# Time: O(n)
# Space: O(1)
# Idea: hold2 only start being larger than 0 when the drop is smaller than the first profit. (1)
#       release2 only start being larger than release1 when hold2 > 0.(1)
# keep tinking!
"""
        1. 1,2,4,2,5,7,2,4,9 (two)
        
           h1   r1   h2   r2
          -inf  0   -inf  0
        1  -1   0    -1   0
        2  -1   1    -1   1
        4  -1   3    -1   3
        2  -1   3     1   3
        5  -1   4     1   6
        7  -1   6     1   8
        2  -1   6     4   8
        4  -1   6     4   8
        9  -1   8     4   13
        
        2. 6,4,3,5,1(one)
        
           h1   r1   h2   r2
          -inf  0   -inf  0
        6  -6   0    -6   0
        4  -4   0    -4   0
        3  -3   0    -3   0
        5  -3   2    -3   2
        1  -1   2    -1   2
        
        3. 1,2,3(one)
        
           h1   r1   h2   r2
          -inf  0   -inf  0
        1  -1   0    -1   0
        2  -1   1    -1   1
        3  -1   2    -1   2
        
        4. 3,2,1(zero)
        
           h1   r1   h2   r2
          -inf  0   -inf  0
        3  -3   0    -3   0
        2  -2   0    -2   0
        1  -1   0    -1   0
        """
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1, release1, hold2, release2 = float('-inf'), 0, float('-inf'), 0
        for p in prices:
            release2 = max(release2, hold2 + p)
            hold2 = max(hold2, release1 - p)
            release1 = max(release1, hold1 + p)
            hold1 = max(hold1, -p)
            
        return release2
