"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""

# ============= Binary Search ===========
# Time: O(n)
# Space: O(1)

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n
        
        begin, end = 1, n
        while begin + 1 < end:
            mid = (begin + end)/2
            cur = (mid*(mid + 1))/2 
            if cur == n: return mid
            
            if cur > n:
                end = mid
            else:
                begin = mid
                
        if (end*(end + 1))/2 <= n:
            return end
        return begin
        
# ============== BS 2 ===============
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n
        
        begin, end = 1, n
        while begin <= end:
            mid = (begin + end)/2
            cur = (mid*(mid + 1))/2 
            if cur == n: return mid
            
            if cur > n:
                end = mid - 1
            else:
                begin = mid + 1
                
        return begin - 1
        
# ======== Math =============
# Time: O(1)
# Space: O(1)
# Idea:
"""
k(k + 1)/2 <= n
=> k^2 + k <= 2n
=> (k + 1/2)^2 <= 2n + 1/4
=> k <= (sqrt(8n + 1) - 1)/2
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n*8 + 1) - 1)/2
