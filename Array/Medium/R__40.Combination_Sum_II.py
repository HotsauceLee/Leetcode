#============= Sort + Back-tracking==========
# Time: ?
# Space: ?
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(candidates, target, sum, begin, cur_path, result):
            if sum > target: return
            if sum == target: result.append(cur_path[:])
            
            for i in xrange(begin, len(candidates)):
                if i > begin and candidates[i] == candidates[i-1]: continue
                sum += candidates[i]
                cur_path.append(candidates[i])
                helper(candidates, target, sum, i + 1, cur_path, result)
                cur_path.pop()
                sum -= candidates[i]
                
        result = []
        candidates.sort()
        helper(candidates, target, 0, 0, [], result)
        return result
