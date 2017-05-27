"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

# ============= q ============
# Time: O(1)
# Space: O(k)
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = size
        self.q = collections.deque()
        self.cur_sum = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.cur_sum += val
        self.q.append(val)
        while len(self.q) > self.window:
            popped = self.q.popleft()
            self.cur_sum -= popped
        
        return self.cur_sum*1.0/len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
