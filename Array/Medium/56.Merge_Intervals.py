# =========== Sort ============
# Time: O(nlog(n) + n)
# Space: O(1)
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        if len(intervals) <= 1:
            return intervals
        
        def interval_cmp(i1, i2):
            if i1.start != i2.start:
                return i1.start - i2.start
            return i1.end - i2.end
            
        intervals.sort(cmp=interval_cmp)
        result = []
        i = 0
        while i < len(intervals):
            min_start, max_end = intervals[i].start, intervals[i].end
            while i + 1 < len(intervals) and max_end >= intervals[i + 1].start:
                i += 1
                min_start = min(min_start, intervals[i].start)
                max_end = max(max_end, intervals[i].end)
            result.append(Interval(min_start, max_end))
            i += 1
            
        return result
