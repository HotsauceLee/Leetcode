"""
39. Combination Sum
40. Combination Sum II
78. Subsets
90. Subsets II
46. Permutations
47. Permutations II
131. Palindrome Partitioning
"""

# 39. Combination Sum
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
