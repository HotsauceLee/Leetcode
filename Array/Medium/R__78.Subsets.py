#=========== Back tracking =========
# Time: O(n^2)
# Space: O
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, begin, cur_path, result):
            for i in xrange(begin, len(nums)):
                cur_path.append(nums[i])
                result.append(cur_path[:])
                helper(nums, i + 1, cur_path, result)
                cur_path.pop()
                
        result = [[]]
        helper(nums, 0, [], result)
        return result
