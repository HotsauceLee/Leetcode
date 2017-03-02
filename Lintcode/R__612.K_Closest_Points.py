# ============= Heap + Custom Comparator =============
# Time: O(nlog(n))
# Space: O(n)
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import heapq

class Type:
    def __init__(self, dist, point):
        self.dist = dist
        self.point = point

    def __cmp__(self, other):
        if other.dist != self.dist:
            return other.dist - self.dist
        if other.point.x != self.point.x:
            return other.point.x - self.point.x
        return other.point.y - self.point.y

class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        # O(nlog(k)) + O(k)
        self.heap = []
        # O(n)
        for point in points:
            dist = self.getDistance(point, origin)
            # log(k)
            heapq.heappush(self.heap, Type(dist, point))
            # log(k)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

        ret = []
        # O(k)
        while len(self.heap) > 0:
            ret.append(heapq.heappop(self.heap).point)
        
        # O(k)
        ret.reverse()
        return ret
            
    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
