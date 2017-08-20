"""
Ugly number is a number that only have factors 2, 3 and 5.

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

 Notice

Note that 1 is typically treated as an ugly number.

Have you met this question in a real interview? Yes
Example
If n=9, return 10.
"""
# ============= Heap keep adding newly generated uglies ===========
# Time: O(n3log(n))
# Space: O(3n^2)
import heapq
class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if n < 1: return None
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 3
        
        heap = [2, 3, 5]
        d = set(heap)
        result = None
        for i in xrange(n-1):
            result = heapq.heappop(heap)
            for j in [2, 3, 5]:
                cur_ugly = j * result
                if cur_ugly not in d:
                    d.add(cur_ugly)
                    heapq.heappush(heap, cur_ugly)
                    
        return result
