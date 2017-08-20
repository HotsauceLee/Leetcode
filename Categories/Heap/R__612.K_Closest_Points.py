"""
Given some points and a point origin in two dimensional space, find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.

Have you met this question in a real interview? Yes
Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
"""
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
