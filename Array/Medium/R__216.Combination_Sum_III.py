#============== Backtracking ===========
# Time: ?
# Space: ?
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(begin, cur_sum, cur_path, result):
            if len(cur_path) == k:
                if cur_sum == n: result.append(cur_path[:])
                return
                
            for i in xrange(begin, 10):
                cur_sum += i
                if cur_sum > n: return
                cur_path.append(i)
                helper(i + 1, cur_sum, cur_path, result)
                cur_path.pop()
                cur_sum -= i
                
        result = []
        helper(1, 0, [], result)
        return result
