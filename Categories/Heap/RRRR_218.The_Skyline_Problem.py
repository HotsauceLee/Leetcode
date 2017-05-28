"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

 Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
Credits:
Special thanks to @stellari for adding this problem, creating these two awesome images and all test cases.
"""

# ============ Heap with delete ============
# Time: O(nlog(n))
# Space: O(n)
class CriticalPoint(object):
    def __init__(self, id, a=True, x=0, h=0, p=-1):
        """
        Need an id to pair start and end so that we know which one to delete.
        """
        self.id = id     # unique identifier
        self.a  = a      # active
        self.x  = x      # point
        self.h  = h      # height
        
    def __cmp__(self, other):
        # python heapq pops the smallest one
        # reverse this to pop the largest one
        return other.h - self.h
        
    def __str__(self):
        return "%s#%s" % (self.id, self.h)


class HeapQueueWithDelete(object):
    def __init__(self):
        self.heap = [CriticalPoint(id=-1)]
        self.delete_map = {}
    
    def push(self, point):
        heapq.heappush(self.heap, point)
        self.delete_map[str(point)] = point
            
    def peak(self):
        while self.heap and not self.heap[0].a:
            heapq.heappop(self.heap)
            
        return self.heap[0]
        
    def delete(self, point):
        pid = point.id
        prev_map_key = "%s#%s" % (pid, -point.h)
        prev_point = self.delete_map.pop(prev_map_key)
        prev_point.a = False


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
            
        critical_points = []
        counter = itertools.count()
        for b in buildings:
            id = next(counter)
            critical_points.append(CriticalPoint(id, True, b[0], b[2]))
            critical_points.append(CriticalPoint(id, True, b[1], -b[2]))
        
        def custom_cmp(a, b):
            return a.x - b.x

        critical_points.sort(cmp=custom_cmp)

        result = []
        heap = HeapQueueWithDelete()
        prev = 0
        i = 0
        while i < len(critical_points):
            while i < len(critical_points):
                cur_cp = critical_points[i]
                # push into heap
                if cur_cp.h > 0:
                    heap.push(cur_cp)
                # delete from heap
                else:
                    heap.delete(cur_cp)
                
                # continue to push/pop the ones at same x
                if i + 1 < len(critical_points) and cur_cp.x == critical_points[i + 1].x:
                    i += 1
                else:
                    break
            
            cur_max = heap.peak()
            if cur_max.h != prev:
                result.append([cur_cp.x, cur_max.h])
                prev = cur_max.h
                
            i += 1
            
        return result
        
