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
    
#=========== sort + back tracking less space and time ===========
# Time: ?
# Space: ?
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, cur_path, result, used):
            if len(cur_path) == len(nums):
                result.append(cur_path[:])
                return
            
            for i in xrange(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                cur_path.append(nums[i])
                used[i] = True
                helper(nums, cur_path, result, used)
                used[i] = False
                cur_path.pop()
        
        nums.sort()     
        result = []
        used = [False]*len(nums)
        helper(nums, [], result, used)
        return result
