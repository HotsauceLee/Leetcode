"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""

# ============= find same slope with gcd =============
# Time: O(n^2)
# Space: O(n^2)
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        lens = len(points)
        if lens <= 2:
            return lens
        
        # Euclid's algorithm
        # https://en.wikipedia.org/wiki/Greatest_common_divisor
        def find_gcd(x, y):
            if y == 0:
                return x
            return find_gcd(y, x%y)
            
        result = 0
        for i in xrange(lens):
            m = {}
            # Find the slopes of every point to this point
            cur_x = points[i].x
            cur_y = points[i].y
            # cur_max record the points with same slopes
            # overlap record the same pooints
            overlap = cur_max = 0
            for j in xrange(lens):
                # skip itself
                if i == j:
                    continue
                
                # find the current difference
                next_x = points[j].x - cur_x
                next_y = points[j].y - cur_y

                # if overlap
                if next_x == 0 and next_y == 0:
                    overlap += 1
                    continue
                
                # WRONG! If same x or same y, they could be in the same
                # horizantal or vertical line
                # if same x or same y, couldn't be on the same line
                # if next_x == 0 or next_y == 0:
                #     continue
                
                # find gcd
                gcd = find_gcd(next_x, next_y)
                if gcd != 0:
                    next_x /= gcd
                    next_y /= gcd

                if next_x in m:
                    if next_y in m[next_x]:
                        m[next_x][next_y] += 1
                    else:
                        m[next_x][next_y] = 1
                else:
                    m[next_x] = { next_y : 1 }
                
                # don't forget i point itself
                cur_max = max(cur_max, m[next_x][next_y])
                
            result = max(result, cur_max + overlap + 1)
                
        return result
                
