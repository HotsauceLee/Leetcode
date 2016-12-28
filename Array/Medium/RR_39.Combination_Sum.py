# ============ Recursion ==============
# Time: ?
# Space: ?

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(candidates, target, sum, begin, cur_path, result):
            if sum > target: return
            if sum == target: result.append(cur_path[:])
            
            for i in xrange(begin, len(candidates)):
                sum += candidates[i]
                cur_path.append(candidates[i])
                helper(candidates, target, sum, i, cur_path, result)
                cur_path.pop()
                sum -= candidates[i]
        
        candidates.sort()
        result = []
        helper(candidates, target, 0, 0, [], result)
        
        return result
