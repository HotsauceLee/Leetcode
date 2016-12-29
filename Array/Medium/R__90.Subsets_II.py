#======= sort + back-tracking =========
# Time: O(n^2)
# Space:
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, begin, cur_path, result):
            for i in xrange(begin, len(nums)):
                if i > begin and nums[i] == nums[i-1]: continue
                cur_path.append(nums[i])
                result.append(cur_path[:])
                helper(nums, i + 1, cur_path, result)
                cur_path.pop()
        
        nums.sort()
        result = [[]]
        helper(nums, 0, [], result)
        return result
