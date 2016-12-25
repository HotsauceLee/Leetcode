#============ Loop ============
# Time: O(n)
# Space: O(1)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows <= 0: return result
        result.append([1])
        if numRows == 1: return result
        
        for i in xrange(numRows - 1):
            cur_level = []
            for j in xrange(len(result[-1]) + 1):
                val = 0
                if j - 1 >= 0:
                    val += result[-1][j - 1]
                if j < len(result[-1]):
                    val += result[-1][j]
                cur_level.append(val)
            result.append(cur_level)
            
        """Shorter loop
        for i in xrange(numRows - 1):
            cur_level = []
            last_lens = len(result[-1])
            for j in xrange(last_lens + 1):
                if j == 0 or j == last_lens:
                    cur_level.append(1)
                else:
                    cur_level.append(result[-1][j - 1] + result[-1][j])
            result.append(cur_level)
        """
            
        return result
        
#============= Offset ============
# Time: O(n)
# Space: ?
def generate(self, numRows):
    res = [[1]]
    for i in range(1, numRows):
        res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]
