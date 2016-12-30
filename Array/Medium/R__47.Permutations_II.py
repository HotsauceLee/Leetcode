#=========== sort + back tracking ===========
# Time: ?
# Space: ?
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, cur_path, result):
            if not nums:
                result.append(cur_path[:])
                return
            
            for i in xrange(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                nums_copy = nums[:]
                cur_path.append(nums[i])
                del nums_copy[i]
                helper(nums_copy, cur_path, result)
                cur_path.pop()
        
        nums.sort()     
        result = []
        helper(nums, [], result)
        return result
