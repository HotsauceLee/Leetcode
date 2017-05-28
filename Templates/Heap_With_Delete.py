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
