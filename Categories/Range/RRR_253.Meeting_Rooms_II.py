"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

# ============= merge intervals ===============
# Time: O(nlog(n))
# Space: O(n)
# Idea: merge the ones that could share a room, otherwise push into heap
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class IntervalWrapper(object):
    def __init__(self, i):
        self.start = i.start
        self.end = i.end
        
    def __cmp__(self, other):
        return self.end - other.end

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(cmp=lambda i1, i2: i1.start - i2.start)
        heap = [IntervalWrapper(intervals[0])]
        for i in xrange(1, len(intervals)):
            min_end = heapq.heappop(heap)
            if intervals[i].start < min_end.end:
                heapq.heappush(heap, IntervalWrapper(intervals[i]))
            else:
                min_end.end = intervals[i].end
            
            heapq.heappush(heap, min_end)
            
        return len(heap)

# ================ same but with pointers ===============
# https://discuss.leetcode.com/topic/35253/explanation-of-super-easy-java-solution-beats-98-8-from-pinkfloyda
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        
        starts.sort()
        ends.sort()
        rooms = end_pos = 0
        for i in xrange(len(starts)):
            if starts[i] < ends[end_pos]:
                rooms += 1
            else:
                end_pos += 1
                
        return rooms
