# =============== Binary Search =================
# Time: O(n + log(n))
# Space: O(1)
"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        begin, end = 0, 1
        while reader.get(end - 1) < target:
            begin = end
            end *= 2
            
        
        while begin + 1 < end:
            mid = (begin + end)/2
            if reader.get(mid) < target:
                begin = mid
            else:
                end = mid
                
        if reader.get(begin) == target:
            return begin
        if reader.get(end) == target:
            return end
            
        return -1
