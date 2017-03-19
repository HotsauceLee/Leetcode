"""
Given an interval list which are flying and landing time of the flight. How many airplanes are on the sky at most?

 Notice

If landing and flying happens at the same time, we consider landing should happen at first.

Have you met this question in a real interview? Yes
Example
For interval list

[
  [1,10],
  [2,3],
  [5,8],
  [4,7]
]
Return 3
"""

# ============== Sort + weight accumulation ==========
# Time: O(k + nlog(n) + n). n - total # of time points. k - # of airplanes
# Space: O(n)
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class TimePoint(object):
    def __init__(self, time, flag):
        self.time = time
        self.flag = flag
        
    def __cmp__(self, other):
        if self.time != other.time:
            return self.time - other.time
        return self.flag - other.flag

class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
        
        point_list = []
        for a in airplanes:
            point_list.append(TimePoint(a.start, 1))
            point_list.append(TimePoint(a.end, 0))
            
        point_list.sort()
        cur_sum = 0
        max_sum = float('-inf')
        for p in point_list:
            if p.flag == 1:
                cur_sum += 1
            else:
                cur_sum -= 1
                
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
