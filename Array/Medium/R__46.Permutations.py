#========= Back tracking using more space ============
# Time: ?
# Space: ?
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, cur_path, result):
            if not nums:
                result.append(cur_path[:])
                return
            
            for idx, n in enumerate(nums):
                # more space
                nums_copy = nums[:]
                cur_path.append(n)
                del nums_copy[idx]
                helper(nums_copy, cur_path, result)
                cur_path.pop()
                
        result = []
        helper(nums, [], result)
        return result
        
#========= Back tracking less time less space ============
# Time: ?
# Space: ?
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, cur_path, result):
            if len(cur_path) == len(nums):
                result.append(cur_path[:])
                return
            
            for n in nums:
                if cur_path.count(n) != 0: continue
                cur_path.append(n)
                helper(nums, cur_path, result)
                cur_path.pop()
                
        result = []
        helper(nums, [], result)
        return result
