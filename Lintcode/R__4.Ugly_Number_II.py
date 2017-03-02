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
