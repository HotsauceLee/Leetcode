#=========== loops ============
# Time: O(k^2)
# Space: O(k)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        if rowIndex <= 0: return result
        
        for i in xrange(rowIndex):
            tmp = 1
            for j in xrange(1, len(result)):
                cur_val = result[j]
                result[j] += tmp
                tmp = cur_val
            result.append(1)
            
        return result
        
#=========== loops backwards ============
# Time: O(k^2)
# Space: O(k)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0]*(rowIndex + 1)
        result[0] = 1
        
        for i in xrange(1, rowIndex + 1):
            j = i
            while j >= 1:
                result[j] += result[j - 1]
                j -= 1
                
        return result
