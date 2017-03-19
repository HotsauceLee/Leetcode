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

# ============= Weight Accumulation ==============
# Time: O(k + max(end))
# Space: O(max(end))
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
        
        max_end = float('-inf')
        for a in airplanes:
            max_end = max(max_end, max(a.start, a.end))

        total_time_span = [0]*(max_end + 1)
        for a in airplanes:
            total_time_span[a.start] += 1
            total_time_span[a.end] -= 1
        
        max_in_the_air = float('-inf')
        weight_so_far = 0
        for i in total_time_span:
            weight_so_far += i
            max_in_the_air = max(max_in_the_air, weight_so_far)
            
        return max_in_the_air
