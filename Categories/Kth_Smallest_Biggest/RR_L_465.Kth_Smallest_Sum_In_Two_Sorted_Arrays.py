# =========== heap + hashset ===========
# Time: O(k*3*log(k^2)) = O(klog(k))
# Space: heap: O(n) set: O(k)
# Trap: don't push visited in to the heap again
class Node(object):
    def __init__(self, val, a, b):
        self.val = val
        self.a = a
        self.b = b
        
    def __cmp__(self, other):
        return self.val - other.val

import heapq
class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if not A and not B:
            return None
        if not A:
            return B[k-1]
        if not B:
            return A[k-1]
        if k == 1:
            return A[0] + B[0]
            
        heap = [Node(A[0] + B[0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        result = None
        # O(k)
        while k >= 1:
            # log(n)
            cur_smallest = heapq.heappop(heap)
            result, a, b = cur_smallest.val, cur_smallest.a, cur_smallest.b
            k -= 1
            if a + 1 < len(A) and (a + 1, b) not in visited:
                # log(n)
                heapq.heappush(heap, Node(A[a+1] + B[b], a + 1, b))
                visited.add((a + 1, b))
            if b + 1 < len(B) and (a, b + 1) not in visited:
                # log(n)
                heapq.heappush(heap, Node(A[a] + B[b+1], a, b + 1))
                visited.add((a, b + 1))
                
        return result
