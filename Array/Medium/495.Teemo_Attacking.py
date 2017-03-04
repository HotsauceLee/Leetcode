# ============ Loop ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        if len(timeSeries) == 1:
            return duration
        if duration == 0:
            return 0

        result = duration
        start, end = timeSeries[0], timeSeries[0] + duration
        for t in xrange(1, len(timeSeries)):
            if timeSeries[t] <= end:
                result += timeSeries[t] + duration - end
                end = timeSeries[t] + duration
            else:
                result += duration
                start, end = timeSeries[t], timeSeries[t] + duration
                 
        return result
